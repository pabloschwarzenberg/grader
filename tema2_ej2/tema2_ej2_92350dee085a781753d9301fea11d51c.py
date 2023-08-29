# completa el código de la función
def suma_divisores(num):
    suma=0
    i=1
    while i<=num-1:
        if num%i==0:
            suma=suma+i
        i=i+1
    return suma

def amigos(a,b):
    if suma_divisores(a)==b and suma_divisores(b)==a:
        return True
    return False
if __name__ == "__main__":
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    c=amigos(n1,n2)
    print(c)

