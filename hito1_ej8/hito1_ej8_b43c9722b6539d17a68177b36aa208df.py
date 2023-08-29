#Descomponer un número
numero = int(input ("ingrese numero a descomponer"))
miles= numero//1000
resto= numero%1000
centenas= resto//100
resto = resto % 100
decenas = resto // 10
unidades = resto % 10
print (miles,"M+",centenas,"C+",decenas,"D+",unidades,"U")