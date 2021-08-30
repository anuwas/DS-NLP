import nltk

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

sentence_1="NLP is an elective course"
sentence_2="NLP course is relevant for data science and data engineering"
sentence_3="Shyam performed better than Amina in NLP course"
sentence_4="Amina performed better than Shyam in NLP course"

analyzer = CountVectorizer().build_analyzer()


def stemmed_words(doc):
    return (PorterStemmer().stem(w) for w in analyzer(doc))

CountVec = CountVectorizer(stop_words='english',ngram_range=(1,1))

# Transform
Count_data = CountVec.fit_transform([sentence_1,sentence_2,sentence_3,sentence_4])
print(CountVec.get_feature_names())
#create dataframe
cv_dataframe=pd.DataFrame(Count_data.toarray(),columns=CountVec.get_feature_names())
print(cv_dataframe)

# Examaple of tf-idf
print("TF-IDF Example ------------------------")

corpus = [
'NLP is an elective course',
'NLP course is relevant for data science and data engineering',
'Shyam performed better than Amina in NLP course',
'Amina performed better than Shyam in NLP course',
]
vectorizer = TfidfVectorizer(stop_words='english',ngram_range=(1,1))
X = vectorizer.fit_transform(corpus)
#create dataframe
cv_dataframe=pd.DataFrame(X.toarray(),columns=vectorizer.get_feature_names())
print(cv_dataframe)