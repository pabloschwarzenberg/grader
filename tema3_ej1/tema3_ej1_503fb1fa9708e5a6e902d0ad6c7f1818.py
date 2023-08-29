# completa el código de la función
def suma_divisores(a):
  return
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma


numero = int(input("Ingresa el número: "))
print("La suma es de sus divisores es: ")
print(suma_divisores(numero))