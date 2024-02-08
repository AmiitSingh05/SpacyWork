"""
Part of speech or POS:  explains how a particular word is used in a sentence. Parts of speech are 8:
Noun , Pronoun, Adjective, Verb, Adverb, Preposition, Conjunction, Interjection
"""

import spacy
from base_functions import get_docs

doc = get_docs()
print("Token","          ","Tag","          ","POS","          ","Explanation")
print("____________________________________________\n")
for token in doc:
    print(token.text,"          ", token.tag_,"         ", token.pos_,"         ", spacy.explain(token.tag_))