#! /usr/local/bin/python3
from render import *
import webbrowser


print("Welcome to CS166-Levenshtein Automation Walker !")
print("-------------------------------------------------")
while 1:
    print("Type your word for Levenshtein, test word and max edit distance like: <Levenshtein_Word> <Test_Word> k")
    print("Your input: ")
    user_input = input()
    if (user_input == "exit"): 
        print("-=-=-=- Bye --=-=-= ")
        exit() 
    words = user_input.split()
    if len(words) != 3:
        print("Invalid input >_<")
        continue 
    w, test_w, k = words
    output = render(w, test_w, int(k))
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    webbrowser.open('file://' + os.path.realpath(output))
    print()
    print()
    
