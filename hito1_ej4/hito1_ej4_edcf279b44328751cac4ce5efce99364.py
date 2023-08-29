#Conversión de Decimal a Binario
#reciba como entrada un número decimal e imprima el resultado de convertirlo a binario. 
decimal= int(input("ingrese numero decimal: "))
lista_modulos = [ ]
while decimal != 0:
       modulo = decimal % 2
       cociente = decimal //  2
       # print("COCIENTE::: "+ str(cociente))
       lista_modulos.append(str(modulo))
       decimal = cociente
print("resultado=" + "".join(lista_modulos[::-1]))
