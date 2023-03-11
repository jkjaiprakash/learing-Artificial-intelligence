# Text Preprocessing

# var="india is my country and i am from tamilnadu"
# print(var.split())

# # import nltk
# # nltk.download('punkt')   -  Downloads a package inside nltk
# import nltk
# nltk.download('stopwords') -  Downloads a package inside nltk

# var="India is my Country and i am from Tamilnadu"
# from nltk.tokenize import word_tokenize
# words=word_tokenize(var)
# print(words)
# lower=[]
# for x in words:
#     lower.append(x.lower())
# print(lower)

# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# stop_words=set(stopwords.words("english"))
# word_tokens=word_tokenize(var)
# filtered_sentence = [x for x in word_tokens if x not in stop_words]
# print(filtered_sentence)

#   Stemming

# from nltk.stem import PorterStemmer
# a=PorterStemmer()
# b="India is my Country and i am from Tamilnadu"
# for x in b.split():
#     print(a.stem(x))

# from nltk.stem import PorterStemmer
# a=PorterStemmer()
# b="Machine learning school"
# for x in b.split():
#     print(a.stem(x))

#  Lemmatzation
import nltk
# from nltk.stem import WordNetLemmatizer
# # nltk.download('wordnet')
# a=WordNetLemmatizer()
# b=a.lemmatize("machine",pos="n")
# print(b)

# from nltk.stem import WordNetLemmatizer
# a=WordNetLemmatizer()
# b=a.lemmatize("learning",pos="v")
# print(b)

# import nltk
# nltk.download('averaged_perceptron_tagger')
# var = "Machine learning"
# from nltk import pos_tag
# z = pos_tag(var.split())
# print(z)
# short={"NN":"n","VBN":"v","JJ":"a"}
# for x,y in z:
#     b= a.lemmatize(x,pos=short[y])
# print(b)

# var = " I am studying in besant technologies in tambaram"
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
# a = CountVectorizer()
# b=a.fit(var.split())
# print(b.vocabulary_)
# b=a.transform(var.split())
# print(b.toarray())

# How yield works :
# def fun(a,b):
#     yield a+b
# print(fun(10,20))

# def fun(a,b):
#     yield a+b
# for x in fun(10,20):
#     print(x)

# Import package
# import nltk
# nltk.download('twitter_samples')

# ----------------------------------------------------------------------------------------------------------##

# N - Gram

# var = "india is my country and i ma from tamilnadu"
# def ngramm(text, n):
#     ngrams_list = []
#     for num in range(0, len(text)):
#         ngram = ' '.join(text[num:num + n])
#         ngrams_list.append(ngram)
#         return ngrams_list
# text = ngramm(var,2)

# def ngram(text,n):
#     words = text.split()
#     sent=[]
#     for i in range(len(words)-n+1):
#         sent.append(words[i:i+n])
#     print(sent)
# text = ngram(var,5)

# ----------------------------------------------Name Entity Recognization NER-----------------------------------------#

# Identifing the Organizations or a famous person place is known as NER, Example - Place person organization time object

import spacy
NER = spacy.load("en_core_web_sm")
text = "The Indian research organization is the national space agency of india, headquartered in Bengaluru. It operates under Department of space which is owned by the prime Dhoni while the chairman of ISRO acts as am executive officer"
a=NER(text)
for x in a.ents:
    print(x.text,x.label_)

from spacy import displacy
c = spacy.explain("ORG")
d = spacy.explain("GPE")
print(c)
print(d)
data = displacy.render(a,style="ent")
with open("sample.html","w") as var:
    var.write(data)
