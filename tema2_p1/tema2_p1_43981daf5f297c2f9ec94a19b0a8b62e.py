
n = int(input("n="))



def is_prime(n): 
    for i in range(1, n):
        if n % i == 0:
            return False
    return True


print(is_prime(n))
