def checkPrimeNumberRecursive(n, i=2): # Works for small numbers
    if n == 1:
        return False
    if n == i:
        return True
    elif n % i == 0:
        return False
    return checkPrimeNumberRecursive(n, i + 1)

# Due the stack depth allowed by a recursive call, I am going to use a for loop to check for the prime number
def checkPrimeNumber(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

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
    printTheList(palindromeList[::-1])

if __name__ == "__main__":
    main()