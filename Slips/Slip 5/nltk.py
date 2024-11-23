# Q.1) Write a python program to implement Lemmatization using NLTK
# Ans:-
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')

def lemmatize_text(text):

    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    lemmatized_tokens = [lemmatizer.lemmatize(token, get_pos_tag(token)) for token in
    tokens]
    lemmatized_text = ' '.join(lemmatized_tokens)

    return lemmatized_text

def get_pos_tag(word):

    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R":
    wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

# Example usage
input_text = "The cats are running and playing in the garden"
lemmatized_text = lemmatize_text(input_text)

print("Original Text:", input_text)
print("Lemmatized Text:", lemmatized_text)