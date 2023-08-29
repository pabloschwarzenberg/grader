n_1 = 4
n_2 = 3

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
 
if numeros_amigos(n_1,n_2):
    print('True')
    
else:
    print('False')