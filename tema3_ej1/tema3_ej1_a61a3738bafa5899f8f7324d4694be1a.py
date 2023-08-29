# completa el código de la función
 def sumaDivisores(n):
    suma = 0

    for i in range(1, n + 1):
        if n%i == 0:
            suma += i
            return suma
  

print(sumaDivisores(n))

 
def es_primo(n):
    if n< 2:
        return False
    for i in range(2, n):
        if n% i == 0:
            return False
    return True

print(es_primo(n))


if __name__ == '__main__':
  
    