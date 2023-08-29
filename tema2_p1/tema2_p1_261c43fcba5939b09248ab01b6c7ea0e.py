def es_primo(n): 
    for i in range(1, n):
        if n % i == 0:
            return False
    return True

n = int(input("n="))
 print(es_primo(n))1

           