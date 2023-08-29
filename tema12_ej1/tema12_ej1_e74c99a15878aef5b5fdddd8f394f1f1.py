def imprimir(n,numero=""):
    if n==0:
        print(numero)
    else:
        numero1=numero+"0"
        imprimir(n-1,numero1)
        numero2=numero+"1"
        imprimir(n-1,numero2)
n=int(input())
imprimir(n)