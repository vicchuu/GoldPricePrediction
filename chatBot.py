from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
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

print("Hi i'm Vichu chat Bot ,")
while True:

    text = input("How can i help you ..!")
    if text =="Exit":
        break
    print(vichu.get_response(Statement(text=text,search_text=text)))