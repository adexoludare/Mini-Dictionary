"""
    This dictionary module give you the meaning of word.
    if the word you typed in is not in it, the dictionary return the word
    'The word dosen't exit. Please double check it'
"""
import json     # here we import json file where the words and the meaning ware saved
data = json.load(open("data.json")) #load the file and assign it to variable 
from difflib import get_close_matches

def Dictionary(word):
    word = word.lower() # this convert word to lower case since our dictonary only contain lower case word
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0 :
        guess = (get_close_matches(word,data.keys()))
        if len(guess) < 3:
            return "The word dosen't exit. Please double check it"
        else:

            print("the word is wrongly typed the likely correct word are :", guess)
            A = get_close_matches(word,data.keys())[0]
            B = get_close_matches(word,data.keys())[1]
            C = get_close_matches(word,data.keys())[2]
            print('Did you mean {} or {} or {} instead ?'.format(A,B,C,))
            yn = input("Enter A if you mean {} or B if you mean {} or C if you mean {}:" .format(A,B,C)).upper()
            if yn == "A":
                print(A)
                return data[A]
            elif yn == "B":
                print(B)
                return data[B]
            elif yn == "C":
                print(C)
                return data[C]
            else:
                return "we didn't understand your entry."

    else:
        return "The word dosen't exit. Please double check it"


word = input("Enter a word :")

output = (Dictionary(word))

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)

#print(data.keys())