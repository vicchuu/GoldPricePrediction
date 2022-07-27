import nltk
# import ssl
#
# try: #punkt is already uptodate
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download('punkt')

from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()


def tokenise(data):
    return nltk.word_tokenize(data)  # it eill tokenize with predefined words in punkt


def stemming(data):  # stemmer techniques is

    return stemmer.stem(data.lower())


def bagofWords(words):
    pass


# a = "Hi Vishnu how are you in life  life ? *  7  aren't"
#
# v = tokenise(a)
#
# t=["filming","films","film"]
# for a in t:
#     print("Stemming :", stemming(a)) #working fine
