import spacy

def detect_sentence_from_text(input_text):
    """
    This function accepts input text and detect the sentences within 
    the text and returns list of such sentences
    :param input_text: text
    :return: list
    """
    nlp = spacy.load('../../en_core_web_sm')
    about_doc = nlp(input_text)
    sentences = list(about_doc.sents)
    return sentences


# way to call function
input_text = (
             "Amiit Singh is a Python developer currently"
             " working with XYZ company in Bangalore."
             " His interests includes" 
             " Natural Language Processing."
             "He has experience in python , kafka, aws, deep learning"
             " and NLP."
         )
sentences = detect_sentence_from_text(input_text)
for sentence in sentences:
    print("sentence : ",sentence)
