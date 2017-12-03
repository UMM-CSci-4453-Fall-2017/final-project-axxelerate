import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
import string

def stemming(query, n):
    return zip(*[query[i:] for i in range(n)])

def query(query):
    query = query.strip().lower()
    query = query.translate(string.maketrans("",""), string.punctuation).split(' ')
    stop_words = set(stopwords.words('english'))
    query = [word for word in query if word not in stop_words]
    ngrams_query = []
    for i in range(len(query)+1):
        ngrams_query.append(stemming(query, i))
    return ngrams_query
