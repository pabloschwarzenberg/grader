#Descomponer un número
s=int(input('Ingrese un numero de 4 digitos como max:'))
pdigito=s//1000
sdigito=(s//100)%10
tdigito=(s%100)//10
cdigito=s%10


print(pdigito,'M' , '+', sdigito,'C' , '+', tdigito,'D' , '+' , cdigito,'U')
def es_primo(numero):
    if numero < 2:
        return False

    for num in range(2,numero):
        if numero%num == 0:
            return False

    return True
def amigos(x,y):
    suma_x=0
    suma_y=0
    for i in range(1,x):
        if x%i==0:
            suma_x+=i
 
    for k in range(1,y):
        if y%k==0:
            suma_y+=k

    return suma_x==y and suma_y==x
    if suma_x == y and suma_y == x:
        return True
    else:
        return False