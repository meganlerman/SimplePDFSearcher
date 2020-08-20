import PyPDF2  # learn more: https://python.org/pypi/PyPDF2
from nltk import word_tokenize
import nltk
import sklearn
import collections
from nltk.corpus import stopwords
#nltk.download('stopwords')
nltk.download('punkt')
print("Start PDF import...")

def setup():
  filename = "NAWCWD TP 8347.pdf"
  newfile = open(filename, "rb")
  fileReader2 = PyPDF2.PdfFileReader(newfile)

  #print("PDF import complete")
  #print("{} contains {} pages".format(filename , fileReader2.numPages))


  tokens = []
  for num in range(0, fileReader2.numPages):
    tokens += word_tokenize(fileReader2.getPage(num).extractText())
    print(".")



  stemmer = nltk.PorterStemmer()
  tokens = [stemmer.stem(t) for t in tokens]

def process_text(stem=True):

  filename = "NAWCWD TP 8347.pdf"
  newfile = open(filename, "rb")
  fileReader2 = PyPDF2.PdfFileReader(newfile)
  tokens = []
  for num in range(0, fileReader2.numPages):
    tokens += word_tokenize(fileReader2.getPage(num).extractText())
 
    if stem:
        stemmer = nltk.PorterStemmer()
        tokens = [stemmer.stem(t) for t in tokens]
 
    return tokens
 
 
def cluster_texts(texts, clusters=3):
    """ Transform texts to Tf-Idf coordinates and cluster texts using K-Means """
    vectorizer = sklearn.feature_extraction.text.TfidfVectorizer(tokenizer=process_text,
                                 stop_words=stopwords.words('english'),
                                 max_df=0.5,
                                 min_df=0.1,
                                 lowercase=True)
 
    tfidf_model = vectorizer.fit_transform(texts)
    km_model = sklearn.KMeans(n_clusters=clusters)
    km_model.fit(tfidf_model)
 
    clustering = collections.defaultdict(list)
 
    for idx, label in enumerate(km_model.labels_):
        clustering[label].append(idx)
 
    return clustering
 
 
if __name__ == "__main__":
    articles = process_text()
    clusters = cluster_texts(articles, 7)
    print(dict(clusters))
  #print(len(tokens))