# completa el código de la función
def suma_divisores(numero):
    suma = 0
      for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma
    
numero = 15
print("divisor es: ")
print(suma_divisores(numero))