l = int(input("numero: "))
def descomponer(n):
    primo = []
    
    for i in range(2 , n+1):
        while n % i == 0:
            primo.append(i)
            n = n / i
            print(i)
    
    return primo
descomponer(l)