import pathlib
import spacy



def txt_file_to_token_generator(file_name):
    """
    This function read the qualified file_name and generates and return the token
    :param file_name: file path with filename
    :return: list of token
    """
    nlp = spacy.load('../en_core_web_sm')
    introduction_doc = nlp(pathlib.Path(file_name).read_text(encoding="utf-8"))
    token_list = [token.text for token in introduction_doc]
    print ("Info : ",token_list)
    return token_list


# way to call the function
file_name = 'introduction.txt'
print(txt_file_to_token_generator(file_name))