# completa el código de la función
def amigos(a,b):
    i=1
    k=1
    suma1=0
    suma2=0
    while i<a-1:
        if a%i==0:
            suma1+=i
        i=i+1
    while k<b-1:
        if b%k==0:
            suma2+=k
        k=k+1
    if suma1==b:
       if suma2==a:
         return True
    return False

           