#Factores Primos
def primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def factores_primos(a):
    if primo(a):
        print(a)
        return None
    
    else:    
        for i in range(2, a):
            if primo(i):
                if a % i == 0:
                    print(i)
                    return factores_primos(a//i)
            

factores_primos(int(input()))