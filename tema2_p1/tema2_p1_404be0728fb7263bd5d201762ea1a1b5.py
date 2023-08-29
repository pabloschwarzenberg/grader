# por favor escribe aquí tu función
n = int()
def es_primo(n):
    if n==1:
        return False
    elif n ==2:
        return True
    else: 
        for i in range (2, n):
            if n% i ==0:
                return False
        return True
   
print(es_primo(n)) 