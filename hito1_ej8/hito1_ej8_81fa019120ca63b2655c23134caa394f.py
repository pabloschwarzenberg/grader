#Descomponer un número
numero = int(input("ingrese numero hasta 4 digitos: "))
#m=mil
#c=centena
#d=decena
#u=unidad
m = numero//1000
m2 = m%1000

c = numero//100
c2 = c%10

d = numero//10
d2 = d%10

u = numero%10

print(m2,"M", "+", c2,"C", "+", d2,"D", "+", u,"U")
