# Números Amigos
# Números Amigos
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
 
n_1 = int(input("Introduzca el n1: "))
n_2 = int(input("Introduzca el n2: "))
 
if numeros_amigos(n_1,n_2):
    print('Son amigos')
    
else:
    print('No son amigos')