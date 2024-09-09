# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_multiple(x):
    
    num = 0
    not_found = True

    while not_found:
        num += 1
        for i in range(1,x+1):
            if num % i != 0:
                break
            if i == x:
                not_found = False

    return num

smallest_multiple(10)