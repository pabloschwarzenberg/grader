a=int(input())
b=int(input())
def amigos(a,b):
    divisores_a=[]
    for x in range(1,a):
        if a%x==0:
            divisores_a.append(x)
        else:
            pass
    divisores_b=[]
    for y in range(1,b):
        if a%y==0:
            divisores_b.append(y)
        else:
            pass
    suma_a=0
    suma_b=0
    for divisor in divisores_a:
        suma_a+=divisor
    for divisor in divisores_b:
        suma_b+=divisor
    if suma_a==suma_b:
        print("True")
        return True
    else:
        print("False")
        return False
amigos(a,b)
        
           