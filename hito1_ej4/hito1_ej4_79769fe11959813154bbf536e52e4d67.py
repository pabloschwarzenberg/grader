#Conversión de Decimal a Binario
number_1 = int(input("ingrese un numero decimal: "))
lista = []
while number_1>0:
    resto = int(number_1%2)
    lista.append(resto)
    number_1 = (number_1-resto)/2
    number_binario = ""
for e in lista[::-1]:
    number_binario = number_binario + str(e)
print("resultado="+str(number_binario))
