from render import *


print("Welcome to CS166-Levenshtein Automation Walker !")
print("-------------------------------------------------")
while 1:
    print("Type your word for Levenshtein, test word and max edit distance like: <Lev_W> <Test_Word> k")
    print("Your input: ")
    user_input = input()
    if (user_input == "exit"): 
        print("-=-=-=- Bye --=-=-= ")
        exit() 
    words = user_input.split()
    if len(words) != 3:
        print("Invalid input >_<")
    w, test_w, k = words
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    render(w, test_w, int(k))
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print()
