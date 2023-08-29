# completa el código de la función
def es_primo(x):
    if(x==1):
      return False
    for n in range(2, x):
        if x % n == 0:
            
            return False
    
    return True

def suma_divisores(numero=15):
    
    suma = 0
    for i in range(1, numero // 2 + 1):
        if numero % i == 0:
           suma = suma +i
    
    return suma, es_primo(numero)
           