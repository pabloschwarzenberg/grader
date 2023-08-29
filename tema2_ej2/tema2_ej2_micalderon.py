# completa el código de la función
def amigos(a,b):
    contador=1
    contador1=1
    suma=0
    suma1=0
    while contador!=a:
        if a%contador==0:
            suma=suma+contador
        contador=contador+1
    while contador1!=b:
        if b%contador1==0:
            suma1=suma1+contador1
        contador1=contador1+1
    
    if suma == b and suma1 == a:
        return True
    else:
        return False
if __name__ == "__main__":
    a=eval(input("Ingrese el primer numero: "))
    b=eval(input("Ingrese el segundo numero: "))
    print(amigos(a,b))