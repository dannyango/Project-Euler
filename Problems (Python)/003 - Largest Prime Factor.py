# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?



def prime_factors(x):

    factor = 2
    while x / factor != 1:
        if x % factor == 0:
            x /= factor
        else:
            factor +=1
    return factor

prime_factors(600851475143)
