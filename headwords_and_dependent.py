import spacy
from spacy import displacy
from base_functions import get_docs, get_doc


text = ("Amiit has interest in python development workc")
doc = get_doc(text)
for token in doc:
    print("head of words :", token.head.text, "dependent : ",token.dep_)

displacy.serve(doc, style='dep', port=5001) # default port is 5000, you can select any