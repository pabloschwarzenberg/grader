#Descomponer un número
numero = int(input("ingrese numero: "))

unidades = numero%10
decenas = numero%100//10
centenas = numero//100%10
miles = numero//1000

print(miles,"M","+",centenas,"C","+",decenas,"D","+",unidades,"U")
      