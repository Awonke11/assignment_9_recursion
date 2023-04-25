def advanceMatch(pattern, word):
    if len(word) == 0 and len(pattern) == 0:
        return True
    
    if len(word) == 0:
        return False
    
    if (pattern[0:1] == "?"):
        return advanceMatch(pattern[1:], word[1:])
    
    if (pattern[0:1] == "*"):
        if pattern[-1:] == "*":
            return True
        if (pattern[-1:] != word[-1:]):
            return False
        else:
            return advanceMatch(pattern[:-1], word[:-1])
    
    if (pattern[0:1] != word[0:1] or pattern[-1:] != word[-1:]):
        return False
    
    return advanceMatch(pattern[1:-1], word[1:-1])

def main():
    loopingCondition = True
    while loopingCondition:
        pattern = input("Enter a pattern (or 'q' to quit): \n")
        if pattern == "q":
            loopingCondition = False
        else:
            word = input("Enter a word: \n")
            if advanceMatch(pattern, word):
                print("It's a match.")
            else:
                print("They don't match.")

if __name__ == "__main__":
    main()