import os

import nltk
import pandas as pd
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.corpus import stopwords

#nltk.download()
#nltk.download('stopwords');

#Read the csv file
imdb = pd.read_csv("government-procurement-via-gebiz.csv")
#lower all the words in the tender_description column
imdb['tender_description'] = imdb['tender_description'].str.lower()

def identify_tokens(row):
    # Collect all the column in tender_description
    tender_description = row['tender_description']
    # Tokenize all the token_description
    tokens = nltk.word_tokenize(tender_description)
    #Taken only words, no punctuation or numbers
    token_words = [w for w in tokens if w.isalpha()]
    return token_words

#Uses the function and turn it into "words", axis=1 is for taking column instead of index.
imdb['words'] = imdb.apply(identify_tokens, axis=1)

#stemming = PorterStemmer() #Changes the stemmer based on the ouput we want.
stemming = LancasterStemmer() #Changes the stemmer based on the ouput we want, LancasterStemmer is better for WordCloud. Example; Supplies will be change to supply instead of Suppli.
def stem_list(row):
    my_list = row['words']
    stemmed_list = [stemming.stem(word) for word in my_list]
    return (stemmed_list)

#Uses the function and turn it into "stemmed_words", axis=1 is for taking column instead of index.
imdb['stemmed_words'] = imdb.apply(stem_list, axis=1)

stops = set(stopwords.words("english"))

def remove_stops(row):
    my_list = row['stemmed_words']
    meaningful_words = [w for w in my_list if not w in stops]
    return (meaningful_words)

#Uses the function and turn it into "stem_meaningful", axis=1 is for taking column instead of index.
imdb['stem_meaningful'] = imdb.apply(remove_stops, axis=1)

def rejoin_words(row):
    my_list = row['stem_meaningful']
    joined_words = ( " ".join(my_list))
    return joined_words

#Uses the function and turn it into "processed", axis=1 is for taking column instead of index.
imdb['processed'] = imdb.apply(rejoin_words, axis=1)

# Load the library with the CountVectorizer method
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

# DTM Function
def plot_10_most_common_words(count_data, count_vectorizer):
    import matplotlib.pyplot as plt
    words = count_vectorizer.get_feature_names()
    total_counts = np.zeros(len(words))
    for t in count_data:
        total_counts += t.toarray()[0]

    count_dict = (zip(words, total_counts))
    count_dict = sorted(count_dict, key=lambda x: x[1], reverse=True)[0:10]
    words = [w[0] for w in count_dict]
    counts = [w[1] for w in count_dict]
    x_pos = np.arange(len(words))

    plt.figure(2, figsize=(15, 15 / 1.6180))
    plt.subplot(title='10 most common words')
    sns.set_context("notebook", font_scale=1.25, rc={"lines.linewidth": 2.5})
    sns.barplot(x_pos, counts, palette='husl')
    plt.xticks(x_pos, words, rotation=90)
    plt.xlabel('words')
    plt.ylabel('counts')
    plt.show()


# Initialise the count vectorizer with the English stop words
count_vectorizer = CountVectorizer(stop_words='english')
# Fit and transform the processed titles
count_data = count_vectorizer.fit_transform(imdb['processed'])
# Visualise the 10 most common words
plot_10_most_common_words(count_data, count_vectorizer)

import warnings

warnings.simplefilter("ignore", DeprecationWarning)
# Load the LDA model from sk-learn
from sklearn.decomposition import LatentDirichletAllocation as LDA


# Helper function
def print_topics(model, count_vectorizer, n_top_words):
    words = count_vectorizer.get_feature_names()
    for topic_idx, topic in enumerate(model.components_):
        print("\nTopic #%d:" % topic_idx)
        print(" ".join([words[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))


# Tweak the two parameters below if necessary
number_topics = 5
number_words = 10
# Create and fit the LDA model
lda = LDA(n_components=number_topics, n_jobs=-1)
lda.fit(count_data)
# Print the topics found by the LDA model
print("Topics found via LDA:")
print_topics(lda, count_vectorizer, number_words)


from pyLDAvis import sklearn as sklearn_lda
import pickle
import pyLDAvis

LDAvis_data_filepath = os.path.join('ldavis_prepared_' + str(number_topics))
# # this is a bit time consuming - make the if statement True
# # if you want to execute visualization prep yourself
if 1 == 1:
    LDAvis_prepared = sklearn_lda.prepare(lda, count_data, count_vectorizer)
with open(LDAvis_data_filepath, 'w') as f:
    pickle.dump(LDAvis_prepared, f)

# load the pre-prepared pyLDAvis data from disk
with open(LDAvis_data_filepath) as f:
    LDAvis_prepared = pickle.load(f)
pyLDAvis.save_html(LDAvis_prepared, 'ldavis_prepared_' + str(number_topics) + '.html')