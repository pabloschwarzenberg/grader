# completa el código de la función
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
 

n_a=eval(input('Introduzca el nº a: '))
n_b=eval(input('Introduzca el nº b: '))
 
if numeros_amigos(n_a,n_b):
    print ('True')
else:
    print ('False')