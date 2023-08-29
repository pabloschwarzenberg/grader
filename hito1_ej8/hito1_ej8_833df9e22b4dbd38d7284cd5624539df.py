#Descomponer un número
numero=int(input("ingrese un numero:"))
unidades=int(numero%10)
decenas=int((numero%100-numero%10)/10)
centenas=int((numero%1000-numero%100)/100)
miles=int(numero//1000)

print(miles,"M+",centenas,"C+",decenas,"D+",unidades,"U")
