message = input("Enter a message: \n")

def countOccurances(msg):
    if (len(msg) == 0):
        return 0
    
    if (msg[0:1] == msg[1:2]):
        return countOccurances(msg[1:]) + 1
    
    return countOccurances(msg[1:])

print("Number of pairs:", countOccurances(message))