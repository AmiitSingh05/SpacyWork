"""
extracting words those are nouns in noun_list, pronoun in pronoun_list
"""

import spacy
from base_functions import get_docs

doc = get_docs()
noun_list = []
pronoun_list = []
proper_noun_list = []

for token in doc:
    if token.pos_ == "NOUN":
        noun_list.append(token)
    if token.pos_ == "PRONOUN":
        pronoun_list.append(token)
    if token.pos_ == 'PROPN':
        proper_noun_list.append(token)
print("NOUN: ",noun_list,'\n','PRONOUN:',pronoun_list,'\n', 'PROPER NOUN:',proper_noun_list )
