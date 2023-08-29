#Descomponer un número
numero= int(input("Ingrese numero de hasta 4 digitos: "))
milesima= numero//1000
centena= ((numero//100)%10)
decena=  ((numero//10)%10)
unidad= (numero%10)
print(numero)
print(milesima,"M +",centena,"C +",decena,"D +", unidad,"U")   