# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(y):
    
    x = str(y)
    i = 0
    for i in range(len(x)//2):
        if x[i] != x[-(i+1)]:
            return False
    return y

def product(x, y):
    big = i = j = 1

    while i <= x:
        while j <= y:
            if palindrome(i*j) and i*j > big:
                big = i*j
            j += 1
        i += 1
        j = 0

    return big

product(999,999)
