# Q.1) Write a python program to remove stop words for a given passage from a
# text file using NLTK2.
# Ans:-

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

def remove_stop_words(file_path):
    with open(file_path, 'r') as file:
    passage = file.read()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(passage)
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text

# Example usage
file_path = 'path/to/your/textfile.txt' # Replace with the actual path to your text file
result_text = remove_stop_words(file_path)
print("Original Passage:")

with open(file_path, 'r') as file:
    print(file.read())
    print("\nPassage after removing stop words:")
    print(result_text)