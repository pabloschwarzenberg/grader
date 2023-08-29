#Descomponer un número
num=input('ingresa numero')
if len(num)==1:
    u=num[0]+ ('U')
    print(u)
if len(num)==2:
    d=num[0]+ ('D')
    u=num[1]+ ('U')
    suma= d + '+' + u
    print(suma)
if len(num)==3:
    c=num[0]+ ('C')
    d=num[1]+ ('D')
    u=num[2]+ ('U')
    suma= c + '+' + d + '+' + u
    print(suma)
if len(num)==4:
    m=num[0]+ ('M')
    c=num[1]+ ('C')
    d=num[2]+ ('D')
    u=num[3]+ ('U')
    suma=  m + '+' + c + '+' + d + '+' + u
    print(suma)
    