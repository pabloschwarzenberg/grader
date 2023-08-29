def suma_numeros(numero):
    suma = (numero * (numero + 1)) / 2
    return suma

numero= int(input("Ingrese un número: "))
resultado= suma_numeros(numero)
print(resultado)
      