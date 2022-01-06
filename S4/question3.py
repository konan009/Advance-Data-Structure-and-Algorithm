def isPrime( n : int, i  : int = 2 ):
    if (n <= 2):
        return True if(n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):
        return True
    return isPrime(n, i + 1)
 
def loop_number(number_from : int , number : int,  array_list : list = [] ):
    if( number_from < number):
        return array_list
    elif(isPrime(number_from)):
        array_list.append(number_from)
    
    number_from = number_from - 1
    return loop_number( number_from , number , array_list)

def optimal_prime(prime_number : int, n : int):
    array = []
    n = prime_number - n
    assert isPrime( prime_number ) == True or n < 0 , "Sorry invalid input" 
    array = loop_number(prime_number - 1 , n )
    return array


prime_number = 23
n = 5

array = optimal_prime(prime_number,n)
print("Prime Number",array)
