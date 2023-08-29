numero = int(input("Ingrese Número a descomponer: "))

unidades = numero%10
numero = numero//10
decenas = numero%10
numero = numero//10
centenas = numero%10
numero = numero//10
unidadesMil = numero%10

print((unidadesMil),"M", "+", (centenas),"C", "+", (decenas),"D", "+", (unidades),"U")