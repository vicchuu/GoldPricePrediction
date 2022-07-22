from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask ,render_template,request


from flask_sqlalchemy import SQLAlchemy
#
# import nltk
# nltk.download('punkt')
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
chat.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vishnu.db'
chat.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(chat)

# db.session.query(db).delete()
# db.session.commit()

"""DB creation in terminal"""
# >>> from chatBot import db
# >>> db.create_all()
# >>>


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200) ,nullable =False)

    def __repr__(self):
        return '<Name %r>'% self.query


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

arithmethic = '+ ,*,/,-,%'
# print("Hi i'm Vichu chat Bot ,")
# while True:
#
#     text = input("How can i help you ..!")
#     if text =="Exit":
#         break
#     print(vichu.get_response(Statement(text=text,search_text=text)))



@chat.route("/")
@chat.route("/home")
def index():
    User.query.delete()
    data =User(question="Hi im alexa , how can i help ?")
    db.session.add(data)
    db.session.commit()
    print("data.....",data)
    #print("Arithmarhic ",(vichu.get_response(Statement(text="2+4",search_text="2+4"))))
    all_orders = User.query.all()
    return render_template("index.html",prediction_text=all_orders)

@chat.route("/predict",methods=['POST','GET'])
def predict():


    if request.method=='POST':
        userText = [str(x) for x in request.form.values()  ]
        ip = str(userText[0])
        entr = User(question=ip)
        if ip.isidentifier():


            #print("*************")
            # for a in userText:
            #     print("text--> ",a)
            #print(userText)
            #print( vichu.get_response(userText[0]))
            response = vichu.get_response(Statement(text=userText[0],search_text=userText[0]))
            res = User(question=str(response))
        else:
            res = User(question=str(retunnAnswer(ip)))
        db.session.add(entr)
        db.session.add(res)
        #print("R   :",response)
        db.session.commit()
        all_orders = User.query.all()
        return render_template('index.html',prediction_text=all_orders)
    else:
        return "hi under cinstructin"



def retunnAnswer(s):
    #print (eval(s))
    emp=""
    for  e in s:
        if  not e.isalpha() or e in arithmethic:
            emp+=e

    print("QQQQQQQQQ ",emp)
    return eval(emp)



# #commit changes
# con.commit()
#
# #close the connection
# con.close()


if __name__ == "__main__":
    chat.run(debug=True)