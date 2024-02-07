import spacy


def getDocFromText(input_text):
    """
    This function accepts input text and return the document object
    :param input_text: text
    :return: doc object
    """
    nlp = spacy.load('../../en_core_web_sm')
    about_doc = nlp(input_text)
    return about_doc


# way to call function
input_text = (
             "Amiit Singh is a Python developer currently"
             " working with XYZ company in Bangalore."
             " His interests includes" 
             " Natural Language Processing."
             "He has experience in python , kafka, aws, deep learning"
             " and NLP."
         )
sentences = getDocFromText(input_text)
for sentence in sentences:
    print(sentence,sentence.idx)
