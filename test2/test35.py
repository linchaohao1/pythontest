import  random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
"class %%%(%%%):":"Make a class named %%% that is-a %%%",
"class %%%(object) :\n\tdef _init_(self,***)":"class %%% has-a _init_ that take self and *** params.",
"3":"3",
"4":"4",
"5":"5",
"6":"6"
}

if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else
    PHRASE_FIRST = False

for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(),encoding = "utf-8"))

def convert(snippet,phrase):
    class_name =
