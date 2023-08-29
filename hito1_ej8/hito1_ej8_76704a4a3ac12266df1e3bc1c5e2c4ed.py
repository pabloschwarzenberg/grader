#Descomponer un número
num=int(input("ingrese un numero: "))
a=num//1000
b=num%1000
c=b//100
d=b%100
e=d//10
f=d%10

print("{} M + {} C + {} D + {} U".format(a,c,e,f))