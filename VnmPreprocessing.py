import re                                               # library for regular expression operations
from nlp_utils import *                                 # library for standardlize VNM, download from https://gist.github.com/nguyenvanhieuvn/72ccf3ddf7d179b281fdae6c0b84942b
from underthesea import word_tokenize, sent_tokenize    # library for VNM word tokenization

# Import the Vietnamese stopwords file, download from: https://github.com/stopwords/vietnamese-stopwords 
f = open('vietnamese-stopwords.txt', 'r')
vnm_stopwords = f.read().splitlines()
f.close()

# Get punctuations sring from NLTK
punctuations = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~…“”–"""

class VnmPreprocessing():
  def __init__(self):
    pass

  def preprocess2sent(self, input):
    text = self.replace_num(input)
    text = self.standardize_unicode(text)
    text = self.standardize_marks(text)
    text = self.lowercasing(text)

    sent_list = sent_tokenize(text)

    return sent_list

  def preprocess2word(self, input):
    text = self.replace_num(input)
    text = self.standardize_unicode(text)
    text = self.standardize_marks(text)

    tokens = word_tokenize(text)
    tokens_clean = self.lower_rm_stopword_punct(tokens)

    return tokens_clean

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

  def standardize_unicode(self, text):
    std_uni_text = convert_unicode(text)
    return std_uni_text

  def standardize_marks(self, text):
    std_marks_text = chuan_hoa_dau_cau_tieng_viet(text)
    return std_marks_text

  def lowercasing(self, text):
    text1 = text
    return text1.lower()
    
  def lower_rm_stopword_punct(self, tokens):
    tokens_clean = []

    for word in tokens:                         # Go through every word in your tokens list
        word = word.lower()                     # Lowercasing
        if (word not in vnm_stopwords and       # remove stopwords
            word not in punctuations):          # remove punctuation
            tokens_clean.append(word)
    return tokens_clean
