# completa el código de la función
def suma_divisores(numero):
    i=1
    contador=0
    while i<numero:
        if (numero%i)==0:
            contador=contador+i
        elif numero==1:
            contador=0
        else:
            contador=contador
        i=i+1
    if contador==1:
        b=True
    elif contador!=1:
        b=False
    return contador,b

if __name__ == "__main__":
    a=int(input())
    print(suma_divisores(a))