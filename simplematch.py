exitBoolean = True

def checkMatch(pattern, word):
    if (len(pattern) != len(word)):
        return False
    
    if (pattern[0:1] == "?"):
        return checkMatch(pattern[1:], word[-1:])
    
    if (pattern[0:1] != word[-1:]):
        return False;
    
    return checkMatch(pattern[1:], word[-1:])

while (exitBoolean):
    pattern = input("Enter a pattern (or 'q' to quit): \n")
    word = ""
    if (pattern == "q"):
        exitBoolean = False
    else:
        word = input("Enter a word: \n")
        if (checkMatch(pattern, word)):
            print("It's a match.")
        else:
            print("They don't match.")
    


