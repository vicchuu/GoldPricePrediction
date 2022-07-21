from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask ,render_template,request


from flask_sqlalchemy import SQLAlchemy

# #connect to SQLite
# con = sql.connect('db_web.db')
#
# #Create a Connection
# cur = con.cursor()
#
# #Drop users table if already exsist.
# cur.execute("DROP TABLE IF EXISTS users")
#
# #Create users table  in db_web database
# sql ='''CREATE TABLE "users" (
#
# 	"qtext"	TEXT
# )'''
# cur.execute(sql)
chat = Flask(__name__)
chat.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
chat.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(chat)




from chatterbot.conversation import Statement
import nltk
import ssl
#nltk.download()
# import nltk
# import ssl
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download()
vichu = ChatBot("vichu")

trainer = ChatterBotCorpusTrainer(vichu)

trainer.train("/Users/vishnubharathi/PycharmProjects/GoldPricePrediction/custom.yml")

# print("Hi i'm Vichu chat Bot ,")
# while True:
#
#     text = input("How can i help you ..!")
#     if text =="Exit":
#         break
#     print(vichu.get_response(Statement(text=text,search_text=text)))



@chat.route("/")
def index():
    con = sql.connect("db_web.db", check_same_thread=False)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from users")
    data = cur.fetchall()
    print("Date :",data)
    return render_template("index.html", prediction_text=data)

@chat.route("/predict",methods=['POST'])
def predict():

    userText = [str(x) for x in request.form.values()  ]
    print("*************")
    # for a in userText:
    #     print("text--> ",a)
    print(userText)
    print( vichu.get_response(userText[0]))
    response = vichu.get_response(Statement(text=userText[0],search_text=userText[0]))
    print("R   :",response)
    return render_template('index.html',prediction_text=' {}'.format(response))



# #commit changes
# con.commit()
#
# #close the connection
# con.close()


if __name__ == "__main__":
    chat.run(debug=True)