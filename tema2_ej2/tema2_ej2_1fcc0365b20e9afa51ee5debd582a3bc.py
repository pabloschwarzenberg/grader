def numeros_amigos(x,y):
    suma_x=0
    suma_y=0
    for i in range(1,x):
        if x%i==0:
            suma_x+=i
 
    for k in range(1,y):
        if y%k==0:
            suma_y+=k
 
    return suma_x==y and suma_y==x
 
     n1=int(input("Introduzca el n 1: "))
     n2=int(input("Introduzca el n 2: "))
 
if numeros_amigos(n1,n2):
    print('Son amigos')
else:
    print('No son amigos')