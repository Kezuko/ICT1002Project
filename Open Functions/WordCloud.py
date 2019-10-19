import nltk
import pandas as pd
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.corpus import stopwords
import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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

#remove all the columns in this list.
cols_to_drop = ['tender_no.', 'agency', 'award_date', 'tender_detail_status', 'supplier_name', 'awarded_amt', 'tender_description', 'words', 'stemmed_words', 'stem_meaningful']
imdb.drop(cols_to_drop, axis=1, inplace=True)

#Create new csv file and store it in the same directory as this python file
imdb.to_csv('WorldCloudUsage.csv', index=False)

#Read first column of csv file to string of words seperated by tab
your_list = []
with open('WorldCloudUsage.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = '\t'.join([i[0] for i in reader])

# lower max_font_size for the Wordcloud image and generate it
wordcloud = WordCloud(background_color='white', max_font_size=40).generate(your_list)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
wordcloud.to_file('WordCloud.png') #Save the figure into the folder
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
