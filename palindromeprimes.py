def checkPrimeNumber(n, i=2):
    if n == i:
        return True
    elif n % i == 0:
        return False
    return checkPrimeNumber(n, i + 1)

def checkPalindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    
    if (word[:1] != word[-1:]):
        return False
    
    return checkPalindrome(word[1:-1])

palindromeList = []
def getPalindromeNumber(start, end):
    if (start == end):
        return 
    
    if checkPalindrome(str(start)) and checkPrimeNumber(start):
        palindromeList.append(start)
        
    return getPalindromeNumber(start + 1, end)

def printTheList(numberList):
    if len(numberList) == 0:
        return
    else:
        print(numberList.pop())
        return printTheList(numberList)
    
def main():
    start = eval(input("Enter the starting point N: \n"))
    end = eval(input("Enter the ending point M: \n"))
    
    getPalindromeNumber(start, end)
    print("The palindromic primes are:")
    printTheList(palindromeList)

if __name__ == "__main__":
    main()