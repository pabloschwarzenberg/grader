# completa el código de la función
def numeros_amigos(x, y):
    suma_x=0
    suma_y=0
    for i in range(1,x+1):
        if x%i==0:
            suma_x+=i
 
    for k in range(1,y+1):
        if y%k==0:
            suma_y+=k
 
    return suma_x==y and suma_y==x
a=0
b=0
numeros_amigos(a,b)

if numeros_amigos(a,b):
    print("True")
else:
    print("False")