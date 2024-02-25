import pickle
import re
import nltk
import numpy as np
import pandas as pd
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from textblob import TextBlob


contractions_dict=pickle.load(open("cont_dic.pkl","rb"))
cv=pickle.load(open("count_vect.pkl","rb"))
lr=pickle.load(open("log_reg.pkl","rb"))
dic=pickle.load(open("social_slang1.pkl","rb"))


def spell_correct(text):
  blob = TextBlob(text)
  return str(blob.correct())

def expand_slang(text):
  return " ".join([dic[word] if word in dic.keys() else word for word in text.split(" ")])

def expand_abbr(text):
  return " ".join([contractions_dict[word] if word in contractions_dict.keys() else word for word in text.split(" ") ])

english_stopwords = set(stopwords.words('english'))

def remove_stopword(text):
  words = word_tokenize(text)
  filtered_words = [word for word in words if word.lower() not in english_stopwords]
  return ' '.join(filtered_words)

ps=PorterStemmer()
def stem_conv(sen):
  words=word_tokenize(sen)
  return " ".join([ps.stem(word) for word in words])

def preprocessing_text(text):
  text=text.strip()
  text=text.lower()
  text=re.sub(r'<[^>]*>',"",text)
  text=re.sub(r'https?://\S+|www\.\S+','',text)
  text=re.sub(r'[!"#$%&()*+,-./:;<=>?@[\\\]^_`{|}~]'," ",text)
  text=expand_slang(text)
  text=expand_abbr(text)
  text=re.sub(r'[^\w\s]','',text)
  text=re.sub(r'\s+',' ',text)
  text=re.sub(r'(\w)\1+','',text)
  text= re.sub(r'(\w)\1{2,}', r'\1', text)
  text=remove_stopword(text)
  text=spell_correct(text)
  text=stem_conv(text)
  return text


def sentiment(text):
  arr = np.array([text])
  transf = cv.transform(arr)
  return lr.predict(transf)[0]



