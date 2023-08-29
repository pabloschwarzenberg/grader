# completa el código de la función
def amigos(a,b):
    if a!=b and a!=1 and b!=2:
        suma_a= 0
        suma_b= 0
        for i in range(1,a):
            if a % i ==0:
                suma_a += i
        for i in range(1,b):
            if b % i ==0:
                suma_b+=i
        if suma_a==b or suma_b==a:
            return True
        else:
            return False
    else:
        return False

           