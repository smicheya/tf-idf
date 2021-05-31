from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import codecs
import re

dataset = codecs.open("all_tops.txt", "r", "utf-8")
        
tfIdfTransformer = TfidfTransformer(use_idf=True)
countVectorizer = CountVectorizer()
wordCount = countVectorizer.fit_transform(dataset)
newTfIdf = tfIdfTransformer.fit_transform(wordCount)
df = pd.DataFrame(newTfIdf[0].T.todense(), index=countVectorizer.get_feature_names(), columns=["TF-IDF"])
df = df.sort_values('TF-IDF', ascending=False)

print (df.head(25))

for i in range(1,4):
    data= codecs.open("file{id}.txt".format(id=i), "r", "utf-8")
    tfIdfTransformer = TfidfTransformer(use_idf=True)
    countVectorizer = CountVectorizer()
    wordCount = countVectorizer.fit_transform(data)
    newTfIdf = tfIdfTransformer.fit_transform(wordCount)
    df_ = pd.DataFrame(newTfIdf[0].T.todense(), index=countVectorizer.get_feature_names(), columns=["TF-IDF"])
    df_ = df_.sort_values('TF-IDF', ascending=False)
    
    print (df_.head(25))
