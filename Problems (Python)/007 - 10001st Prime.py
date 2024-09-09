# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10001st prime number?

#def prime(x):

#i = 0
#target = 6

#while True:
#    i += 1
#    for j in range(1, round(target ** 0.5) + 1):
#        if target % j != 0:
#            break
#        if j == target:
#            print(i)


primes = []
 
# Function to generate N prime numbers using  
# Sieve of Eratosthenes 
def SieveOfEratosthenes(n):
     
    # Create a boolean array "prime[0..n]" and 
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is 
    # Not a prime, else true. 
    prime = [True for i in range(n + 1)] 
     
    p = 2
    while (p * p <= n): 
           
        # If prime[p] is not changed, 
        # then it is a prime 
        if (prime[p] == True): 
               
            # Update all multiples of p 
            for i in range(p * p, n + 1, p): 
                prime[i] = False
                 
        p += 1
       
    # Print all prime numbers 
    for p in range(2, n + 1): 
        if prime[p]: 
            primes.append(p) 

SieveOfEratosthenes(6)