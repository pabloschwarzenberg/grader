#Ordenar tres números

'''Aplicación para odernar los números ingresados de menos a mayor'''

#Variales
primernum=int(input("Ingrese el primer número: "))
segundonum=int(input("Ingrese el segundo número: "))
tercernum=int(input("Ingrese el tercer número:"))
numeros=primernum, segundonum, tercernum

orden=sorted(numeros)

#Resultado final
print(orden)