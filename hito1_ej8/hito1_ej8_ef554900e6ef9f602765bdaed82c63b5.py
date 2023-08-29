#Descomponer un número
numero=int(input("Ingrese numero de hasta 4 digitos: "))
# Unidades
unidades=numero%10
# Decenas
decenas=int((numero%100-unidades)/10)
# Centenas
centenas=int((numero%1000-numero%100)/100)
# Miles
miles=numero//1000
print(miles,"M","+",centenas,"C","+",decenas,"D","+",unidades,"U")