import re
import spacy
from spacy.tokenizer import Tokenizer


custom_nlp = spacy.load("../../en_core_web_sm")
prefix_re = spacy.util.compile_prefix_regex(custom_nlp.Defaults.prefixes)
suffix_re = spacy.util.compile_suffix_regex(custom_nlp.Defaults.suffixes)
custom_infixes = [r"@"]
infix_re = spacy.util.compile_infix_regex(list(custom_nlp.Defaults.infixes) + custom_infixes)
"""
1. Vocab: A storage container for special cases, which is used to handle cases like contractions and emoticons.
2. prefix_search: A function that handles preceding punctuation, such as opening parentheses.
3. suffix_search: A function that handles succeeding punctuation, such as closing parentheses.
4. infix_finditer: A function that handles non-whitespace separators, such as hyphens.
5. token_match: An optional Boolean function that matches strings that should never be split. 
 It overrides the previous rules and is useful for entities like URLs or numbers
"""
custom_nlp.tokenizer = Tokenizer(custom_nlp.vocab,
                                    prefix_search=prefix_re.search,
                                    suffix_search=suffix_re.search,
                                    infix_finditer=infix_re.finditer,
                                    token_match=None,
                                 )

custom_about_text = (
  "Amiit Singh is a Python developer currently"
             " working with XYZ@based company in Bangalore."
             " His interests includes" 
             " Natural Language Processing."
             "He has experience in python , kafka, aws, deep learning"
             " and NLP.")
custom_tokenizer_about_doc = custom_nlp(custom_about_text)
# you will see 3 token for XYZ@based
print([token.text for token in custom_tokenizer_about_doc])
# output: ['Amiit', 'Singh', 'is', 'a', 'Python', 'developer', 'currently', 'working', 'with', 'XYZ', '@', 'based', 'company', 'in', 'Bangalore', '.', 'His', 'interests', 'includes', 'Natural', 'Language', 'Processing', '.', 'He', 'has', 'experience', 'in', 'python', ',', 'kafka', ',', 'aws', ',', 'deep', 'learning', 'and', 'NLP', '.']
