"""
Lemmatization  reduce words to their base or dictionary form, known as the lemma.
For example, the lemma of "running" is "run", and the lemma of "better" is "good".
"""
# You can remove stop words from the input
# text by making use of the .is_stop attribute of each token.
import spacy

nlp = spacy.load("../../en_core_web_sm")
input_text = (
             "Amiit Singh is a Python developer currently"
             " working with XYZ-based company in Bangalore."
             " His interests includes" 
             " Natural Language Processing."
             "He has experience in python , kafka, aws, deep learning"
             " and NLP."
         )
my_doc = nlp(input_text)
for token in my_doc:
     if str(token) != str(token.lemma_):
         print(f"{str(token):>20} : {str(token.lemma_)}")