def isPrime( n : int, i  : int = 2 ):
    if (n <= 2):
        return True if(n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):
        return True
    return isPrime(n, i + 1)
 
n = 23
if(isPrime(n)):
    print("Number is Prime")
else:
    print("Number is not Prime")

