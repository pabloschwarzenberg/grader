def numeros_amigos(a,b):
    suma_a=0
    suma_b=0
    for i in range(1,a):
        if a%i==0:
            suma_a+=i
 
    for k in range(1,b):
        if b%k==0:
            suma_b+=k
 
    return suma_a==y and suma_b==a
 



 
if numeros_amigos(n_1,n_2):
    print ('Son amigos :)')
else:
    print ('No son amigos :(')