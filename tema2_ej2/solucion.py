__version__ = "1.0"

def suma_divisor(a):
    contador=1
    suma=0
    while contador<a:
        if a%contador==0:
            suma+=contador
        contador+=1
    return suma

def amigos(a,b):
    s1=suma_divisor(a)
    s2=suma_divisor(b)
    if s1==b and s2==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    b=int(input("Ingrese b: "))
    print(amigos(a,b))