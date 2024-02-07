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

info = """
1. text_with_ws:  prints the token text along with any trailing space, if present.
2. is_alpha: indicates whether the token consists of alphabetic characters or not.
3. is_punct: indicates whether the token is a punctuation symbol or not.
4. is_stop: indicates whether the token is a stop word or not.
"""
print(info)
for token in sentences:
     print(
         f"{str(token.text_with_ws):22}"
         f"{str(token.is_alpha):15}"
         f"{str(token.is_punct):18}"
         f"{str(token.is_stop)}"
     )

