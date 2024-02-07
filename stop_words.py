"""
Stop words are typically defined as the most common words in a language. In the English language,
some examples of stop words are the, are, but, and they.326 stop words enrolled in spacy.lang.en
"""

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
spacy_stopwords = STOP_WORDS
print(len(spacy_stopwords))
for stop_word in list(spacy_stopwords):
    print(stop_word)

print(list(spacy_stopwords))