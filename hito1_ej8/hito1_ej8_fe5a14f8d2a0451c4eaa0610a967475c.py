#Descomponer un número
num=input('Ingrese un numero de hasta 4 digitos: ')
if len(num)==4:
 m=num[0]+'M'
 c=num[1]+'C'
 d=num[2]+'D'
 u=num[3]+'U'
 print(m,'+',c,'+',d,'+',u)

if len(num)==3:
 c=num[0]+'C'
 d=num[1]+'D'
 u=num[2]+'U'
 print(c,'+',d,'+',u)

if len(num)==2:
 d=num[0]+'D'
 u=num[1]+'U'
 print(d,'+',u)

if len(num)==1:
 u=num[0]+'U'
 print(u)    