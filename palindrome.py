input_string = input("Enter your message: \n")

def checkPalindrome(message):
    if (len(message) == 0 or len(message) == 1):
        return True
    
    if (message[0:1] != message[-1:]):
        return False
    
    return checkPalindrome(message[1:len(message) - 1])

if (checkPalindrome(input_string)):
    print("Palindrome!")
else:
    print("Not a palindrome!")