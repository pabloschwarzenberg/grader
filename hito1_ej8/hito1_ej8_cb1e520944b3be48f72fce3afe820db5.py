#Descomponer un número
n=int(input('Ingrese un numero de 4 digitos:'))
r1=n//1000
a=n%1000
r2=a//100
b=a%100
r3=b//10
r4=b%10
print(str(r1)+'M'+'+'+str(r2)+'C'+'+'+str(r3)+'D'+'+'+str(r4)+'U')
     