# por favor escribe aquí tu función
def es_primo(n):
    if n == 0 or n == 1:
        return False 
    elif n > 1:
        i = 2
        while n % i != 0:
            i += 1
        if i == n:
            return True
        elif i != n:
            return False
