import spacy


def get_docs():
    nlp = spacy.load('../../en_core_web_sm')
    input_text = (
                 "Amiit Singh is a Python developer currently"
                 " working with XYZ-based company in Bangalore."
                 " Amiit interests includes" 
                 " python, Natural Language Processing."
                 "He has experience in python , kafka, aws, deep learning"
                 " and NLP."
             )

    doc = nlp(input_text)
    return doc

def get_doc(text):
    nlp = spacy.load('../../en_core_web_sm')
    doc = nlp(text)
    return doc