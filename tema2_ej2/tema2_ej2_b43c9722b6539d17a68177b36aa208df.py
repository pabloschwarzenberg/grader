# completa el código de la función
def amigos(a,b):
    for i in range(2,b):
        if(b % i==0):
            S=S+i
        return S
sum1,sum2=1,1 
a=int(input("ingrese primer numero= "))
b=int(input("ingrese segundo numero= "))
sum1 = amigos(a, sum1)
sum2 = amigos(b, sum2)
if((sum1==b)and (sum2==a)):
    print("los numeros Si son numeros amigos")
    return True
else:
           print("los numeros No son numeros amigos")
           return False

    
       