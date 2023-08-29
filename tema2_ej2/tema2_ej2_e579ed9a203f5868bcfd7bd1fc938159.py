def numeros_amigos(x,y):
    sumax=0
    sumay=0
    for i in range(1,x):
        if x%i==0:
            sumax+=i
 
    for k in range(1,y):
        if y%k==0:
            sumay+=k
 
    return sumax==y and sumay==x
 
n1=int(input('Introduzca el n 1: '))
n2=int(input('Introduzca el n 2: '))
 
if numeros_amigos(n1,n2):
    return True
else:
    return False
