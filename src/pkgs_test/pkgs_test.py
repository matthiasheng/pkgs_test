import os
import sys
from string import punctuation
from collections import Counter


def load_text(input_file):
        """Load text from a text file and return as a string."""
        with open(input_file, "r") as file:
            text = file.read()
        return text


def clean_text(text):
        """Lowercase and remove punctuation from a string."""
        text = text.lower()
        for p in punctuation:
            text = text.replace(p, "")
        return text


def count_words(input_file):
        """Count unique words in a string."""
        text = load_text(input_file)
        text = clean_text(text)
        words = text.split()
        return Counter(words)


if __name__ == "__main__":
    content = load_text('zen.txt')
    print(f'content: \n{content}')
    clean_content = clean_text(content)
    print(f'clean_content: \n{clean_content}')
    counter_dict = count_words('zen.txt')
    print(f'counter_dict: \n{counter_dict}')
