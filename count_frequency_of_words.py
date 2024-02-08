# count frequency of words or token.

import spacy
from collections import Counter
from base_functions import get_docs

doc = get_docs()
words = [token.text for token in doc if not token.is_stop and not token.is_punct]
print(words)
print(Counter(words))
"""
output:
['Amiit', 'Singh', 'Python', 'developer', 'currently', 'working', 'XYZ', 'based', 'company', 'Bangalore', 'Amiit', 'interests', 'includes', 'Natural', 'Language', 'Processing', 'experience', 'python', 'kafka', 'aws', 'deep', 'learning', 'NLP']
Counter({'Amiit': 2, 'Singh': 1, 'Python': 1, 'developer': 1, 'currently': 1, 'working': 1, 'XYZ': 1, 'based': 1, 'company': 1, 'Bangalore': 1, 'interests': 1, 'includes': 1, 'Natural': 1, 'Language': 1, 'Processing': 1, 'experience': 1, 'python': 1, 'kafka': 1, 'aws': 1, 'deep': 1, 'learning': 1, 'NLP': 1})

"""