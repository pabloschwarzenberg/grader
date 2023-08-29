#Descomponer un número
numero = int(input("ingrese un numero:"))
u = numero%10
numero = numero//10

d = numero%10
numero = numero//10

c = numero%10
numero = numero//10

m = numero%10
numero = numero//10

print(m,"m", "+",c,"c", "+",d,"d", "+",u,"u")