#Descomponer un número
numero = int(input("Ingresa un numero: "))
m=(numero%10000-numero%1000)//1000
c=(numero%1000-numero%100)//100
d=(numero%100-numero%10)//10
u=numero%10

print( repr(m) + "M + " + repr(c) + "C + " + repr(d) + "D + " + repr(u) + "U"  )