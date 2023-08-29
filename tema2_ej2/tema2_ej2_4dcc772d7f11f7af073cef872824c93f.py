# completa el código de la función
a = int(input('Introduzca el nº 1: '))
b = int(input('Introduzca el nº 2: ')) 

def numeros_amigos(a,b):  
    suma_a=0
    suma_b=0
    for i in range(1,a):
        if a%i==0:
            suma_a+=i

    for k in range(1,b):
        if b%k==0:
            suma_b+=k

    return suma_a==b and suma_b==a

if numeros_amigos(a,b): 
    print ('True')
else:
    print ('False')
