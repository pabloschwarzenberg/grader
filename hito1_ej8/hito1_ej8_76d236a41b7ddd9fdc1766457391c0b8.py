n=int(input('Escribe un numero de maximo 4 digitos: '))
u=n%10
x=n%100
d=x//10
y=n%1000
c=y//100
m=n//1000
print(m,'M+',c,'C+',d,'D+',u,'U')
