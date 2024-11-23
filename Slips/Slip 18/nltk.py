# Q.1). Write a python program to remove stop words for a given passage from a
# text file using NLTK?.
# Ans:-

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')

def remove_stop_words(input_text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(input_text)
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

if __name__ == "__main__":
    file_path = 'your_text_file.txt' # Replace with your text file path
try:
    with open(file_path, 'r', encoding='utf-8') as file:
    passage = file.read()
    cleaned_passage = remove_stop_words(passage)
    print("Original Passage:")
    print(passage)
    print("\nPassage after removing stop words:")
    print(cleaned_passage)
except FileNotFoundError:
    print(f"File not found at path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")