import PyPDF2  # learn more: https://python.org/pypi/PyPDF2
from nltk import word_tokenize
import nltk
import sklearn
import collections
import pandas as pd
from nltk.corpus import stopwords
from pprint import pprint
from sklearn.cluster import KMeans
#nltk.download('stopwords')
#nltk.download('punkt')
import matplotlib
matplotlib.use('TkAgg')


from wordcloud import WordCloud
def main():
    print("Start PDF import...")
    filename = "NAWCWD TP 8347.pdf"
    #filename = "sample.pdf"
    newfile = open(filename, "rb")
    fileReader2 = PyPDF2.PdfFileReader(newfile)
    #tokens = []
    #for num in range(0, fileReader2.numPages):
    #    tokens.append(word_tokenize(fileReader2.getPage(num).extractText()))
    print('PDF imported\nExtracting text')
    pages = []
    for num in range(0, fileReader2.numPages):
        pages.append(fileReader2.getPage(num).extractText())
    print('Text extracted\nStemming words')
    stemmer = nltk.PorterStemmer()
    #print(pages)
    stemmed_pages = []
    for page in pages:
        page_list = page.lower().split(" ")
        page = [stemmer.stem(word.lower().replace('\n', '')) for word in page_list]
        page = ' '.join(page)
        stemmed_pages.append(page)
    pages = stemmed_pages
    print('Words stemmed\nCreating wordcloud')
    #pages = [[stemmer.stem(word.lower()) for word in page.split()] for page in pages]
    #print(pages)
    #print(stemmed_pages)
    
    import matplotlib.pyplot as plt

    all_words = ' '.join(pages)
    wordcloud = WordCloud().generate(all_words)

    plt.figure(figsize = (20,20))

    plt.imshow(wordcloud)

    plt.axis("off")

    #plt.show()
    
    print('Wordcloud created\nVectorizing')
    
    vectorizer = sklearn.feature_extraction.text.TfidfVectorizer()
    tfidf_model = vectorizer.fit_transform(pages)
    
    feature_names = vectorizer.get_feature_names()
    dense = tfidf_model.todense()
    denselist = dense.tolist()
    df = pd.DataFrame(denselist, columns=feature_names)
    pprint(df)
    
    
    km_model = KMeans(n_clusters=7)
    print('3')
    km_model.fit(tfidf_model)
    print('4')
    clustering = collections.defaultdict(list)
    print('5')
    for idx, label in enumerate(km_model.labels_):
        print('6')
        clustering[label].append(idx)
    print('7')
    pprint(clustering)
 
 
if __name__ == "__main__":
    main()
    