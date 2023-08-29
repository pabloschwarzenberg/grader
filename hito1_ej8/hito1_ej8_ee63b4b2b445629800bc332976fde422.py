#Descomponer un número
x = int (input ('Ingresa el valor de numero: '))
c1 =( x %10000 - x %1000 )//1000
c2 =(  x %1000 - x %100 )//100
c3 =( x %100 - x %10 )//10
c4 = ( x %10 )
c1 =str(c1)
c2 =str(c2)
c3 =str(c3)
c4 =str(c4)
m="M"
c="C"
d="D"
u="U"
c1 = (c1 + m)
c2 = (c2 + c)
c3 = (c3 + d)
c4 = (c4 + u)

print(c1 ,"+",c2 ,"+",c3,"+",c4)