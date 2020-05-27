"""
Jumble Solver is a utility to solve jumbled words
The utility takes a jumbled word as input and returns possible words that can be formed
using the letters in the jumbled word
"""

import json
import string
import requests
from bs4 import BeautifulSoup as Bs

ALPHABETS = string.ascii_lowercase
OUT_DIR = "data/words"


def get_words_from_internet():
    """
    Gets a list of words from the internet and saves the words with meanings
    in a json format in the ./data/words directory
    """
    url = "http://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_{0}.html"

    for a in ALPHABETS:
        # Print process
        print(f"Getting all the words for alphabet '{a.upper()}'")
        # Make a http GET request to get the HTML content
        response = requests.get(url.format(a)).text

        # parse the html content
        soup = Bs(response, features="html.parser")

        words_dict = []

        for entry in soup.find_all("p"):
            words_entry = entry.text.split(maxsplit=2)
            try:
                words_dict.append({"word": words_entry[0], "meaning": words_entry[2]})
            except:
                print(words_entry)

        word_json = json.dumps(words_dict, indent=2)

        with open(f"{OUT_DIR}/{a}", mode="w+") as f:
            f.write(word_json)

        print(f"Words starting with alphabet {a.upper()} is saved in the path {OUT_DIR}/{a}'")


def get_words_from_json():
    """
    Gets a list of words from locally stored json data
    :return: List of words
    """
    words = list()
    for a in ALPHABETS:
        with open(f"{OUT_DIR}/{a}", mode="r") as f:
            data = f.read()

        for item in json.loads(data):
            words.append(item)
    return words


def find_jumbled_word(jumbled_word):
    """
    Find possible words that can be formed by the letters of the jumbled_word
    :parameter jumbled_word: string
    """
    words = get_words_from_json()
    print(f"Jumbled word is {jumbled_word}")
    possible_words = set()

    for word in words:
        for k, v in word.items():
            if k is not None and k == 'word' and len(v) == len(jumbled_word):
                if ''.join(sorted(v.lower())) == ''.join(sorted(jumbled_word.lower())):
                    possible_words.add(v)
    return possible_words


input_jumbled_word = input("Enter the jumbled word : ")
print()
print(f"Possible words : {find_jumbled_word(input_jumbled_word)}")
