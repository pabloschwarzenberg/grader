#Descomponer un número
x= int(input("Ingresa un numero que tenga hasta 4 digitos"))
a=int(x/1000)
b=int((x-a*1000)/100)
c=int((x-b*100-a*1000)/10)
u=int((x-a*1000-b*100-c*10))

if a!=0:
    print(a, 'M+', b, 'C+', c, 'D+', u, 'U')
if a==0 and b!=0:
    print(b, 'C+', c, 'D+', u, 'U')
if a==0 and b==0 and c!=0:
    print(c, 'D+', u, 'U')
if a==0 and b==0 and c==0 and u!=0:
    print(u, 'U')
     