import nltk

from nltk.corpus import stopwords
from nltk import ngrams
from nltk import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Example of stop words

print(stopwords.words('english'))

# Output
# ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves',
# 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours',
# 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she',
# "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself',
# 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
# 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am',
# 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has',
# 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the',
# 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of',
# 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
# 'through', 'during', 'before', 'after', 'above', 'below', 'to',
# 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under',
# 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where',
# 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other',
# 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too',
# 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've",
# 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn',
# "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn',
# "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',
# "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn',
# "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

# Example of n-grams

sentence = 'Let’s go for the NLP course'
my_ngrams = ngrams(sentence.split(),2)
print(list(my_ngrams))

# Output - [('Let’s', 'go'), ('go', 'for'), ('for', 'the'), ('the', 'NLP'), ('NLP', 'course')]

my_ngrams = ngrams(sentence.split(),3)
print(list(my_ngrams))

# Output - [('Let’s', 'go', 'for'), ('go', 'for', 'the'), ('for', 'the', 'NLP'), ('the', 'NLP', 'course')]

# Stemming Example
porter = PorterStemmer()
print('Stemming : corpora'+' -> '+porter.stem("corpora"))
print('Stemming : corpuses'+' -> '+porter.stem("corpuses"))
print('Stemming : corporation'+' -> '+porter.stem("corporation"))
print('Stemming : corporate'+' -> '+porter.stem("corporate"))

# Output
# corpora -> corpora
# corpuses -> corpus
# corporation -> corpor
# corporate -> corpor

# Lemmatization Example

lemmatizer = WordNetLemmatizer()
print('Lemmatization : corpora'+' -> '+lemmatizer.lemmatize("corpora"))
print('Lemmatization : corpora'+' -> '+lemmatizer.lemmatize("corporation"))
print('Lemmatization : corpora'+' -> '+lemmatizer.lemmatize("corporate"))
print('Lemmatization : Feet'+' -> '+lemmatizer.lemmatize("feet"))

# Output

# Lemmatization : corpora -> corpus
# Lemmatization : corpora -> corporation
# Lemmatization : corpora -> corporate
# Lemmatization : Feet -> foot