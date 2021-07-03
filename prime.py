
# 4. Here is a function to test whether a number is prime or not. Write a few test cases for this function to see if you can catch any errors in the implementation.

#    import math
#
# def isprime(n):
#     if n%2 == 0 or n%3 == 0 or n%5==0:
#         return False
#     for i in range(7, math.floor(math.sqrt(n)), 2):
#         if n%i == 0:
#             return False
#     return True


import math
def isprime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

print(isprime(3))