suma = 0
numero = 0
cantidad = 0
promedio = 0
valor_maximo = numero

while numero !=-1:
    numero = int(input("Ingrese un numero entero")) 
    if numero !=-1:
        suma = suma+numero
        cantidad = cantidad+1
    if numero>valor_maximo:
        valor_maximo=numero
    elif valor_maximo==0:
        valor_maximo="nd"
print("Cantidad=",cantidad)
print("Suma=",suma)
print("Maximo=",valor_maximo)

  