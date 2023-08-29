#Descomponer un número
#Descomposicion de un Numero a M,C,D,U

num= int(input("Ingrese numero hasta 4 digitos : "))
m=int(num/1000)
c=int((num-m*1000)/100)
d=int((num-c*100-m*1000)/10)
u=int((num-m*1000-c*100-d*10))

if m!=0:
    print(m, 'M+', c, 'C+', d, 'D+', u, 'U')
if m==0 and c!=0:
    print(c, 'C+', d, 'D+', u, 'U')
if m==0 and c==0 and d!=0:
    print(d, 'D+', u, 'U')
if m==0 and c==0 and d==0 and u!=0:
    print(u, 'U')
     