import spacy
from base_functions import get_docs
from  spacy import displacy
doc = get_docs()
displacy.serve(doc, style="dep")
