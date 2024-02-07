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
about_doc = nlp(input_text)
print([token for token in about_doc if not token.is_stop])