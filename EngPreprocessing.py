import re                                       # library for regular expression operations

from nltk import word_tokenize, sent_tokenize, download
from nltk.corpus import stopwords               # module for stop words that come with NLTK
from nltk.stem import PorterStemmer             # module for stemming
from nltk.stem import WordNetLemmatizer         # module for lemmatization

# download the English stopwords from NLTK
download('stopwords')
# download the pre-trained Punkt tokenizer for English, using for PorterStemmer module
download('punkt')
# download wornet for English, using for WordNetLemmatizer module
download('wordnet')

# Get punctuations sring from NLTK
punctuations = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~…“”–"""

class EngPreprocessing():
  def __init__(self):
    pass

  def preprocess2sent(self, input):
    text = self.replace_num(input)
    text = self.lowercasing(text)
    sent_list = sent_tokenize(text)

    return sent_list

  def preprocess2word(self, input):
    text = self.replace_num(input)
    text = self.lowercasing(text)
    tokens = word_tokenize(text)
    tokens_clean = self.rm_stopword_punct(tokens)
    tokens_stem = self.stemming(tokens_clean)
    
    return tokens_stem

  def replace_num(self, text):
    newtext = text

    # remove date time ?
    newtext = re.sub(r'\d+[/-]\d+([/-]\d+)*', ' date', newtext)
    newtext = re.sub(r'\d+[:]\d+([:]\d+)*', ' time', newtext)

    # remove currency ?
    # newtext = re.sub(r'\d+([.,]\d+)*$', ' dollar', newtext)
    # newtext = re.sub(r'$\d+([.,]\d+)*', ' dollar', newtext)

    # remove simple int number, float number may be following space or "(" like "(12.122.122)"
    newtext = re.sub(r'-?\d+([.,]\d+)*', ' num', newtext)
    return newtext

  def lowercasing(self, text):
    text1 = text
    return text1.lower()

  def rm_stopword_punct(self, tokens):
    stopwords_english = stopwords.words('english') 
    tokens_clean = []

    for word in tokens:                         # Go through every word in your tokens list
        if (word not in stopwords_english and   # remove stopwords
            word not in punctuations):          # remove punctuation
            tokens_clean.append(word)
    return tokens_clean
    
  def stemming(self, tokens):
    # Instantiate stemming class
    stemmer = PorterStemmer() 

    # Create an empty list to store the stems
    tokens_stem = [] 

    for word in tokens:
        stem_word = stemmer.stem(word)  # stemming word
        tokens_stem.append(stem_word)  # append to the list
    return tokens_stem

  def lemmatize(self, text):
    # Instantiate stemming class
    lemmatizer = WordNetLemmatizer()
    
    # Create an empty list to store the stems
    tokens_lemma = [] 

    for word in tokens:
        lemma_word = lemmatizer.lemmatize(word)  # stemming word
        tokens_lemma.append(lemma_word)  # append to the list
    return tokens_lemma
