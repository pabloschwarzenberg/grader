n = 21
def es_primo(n):
    if n > 2:
        if n == 2:
            return True

        if n%2 == 0:
            return False
       
        if n%2 != 0:
            return True
    else: 
        return False

print(es_primo(n))