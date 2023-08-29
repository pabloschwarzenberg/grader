def amigos(a,b):
    suma_a=0
    suma_b=0
    for i in range(1,a):
        if a%i==0:
            suma_a+=i
    for k in range(1,b):
        if b%k==0:
            suma_b+=k
    return suma_a==b and suma_b==a
n1=5
n2=26
if amigos(n1,n2):
    print ("True")
else:
    print ("False")