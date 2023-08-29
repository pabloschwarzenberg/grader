#Conversión de Decimal a Binario
def binario(e):
    r=0
    if e>=128:
        e-=128
        r+=10000000
    if e>=64:
        e-=64
        r+=1000000
    if e>32:
        e-=32
        r+=100000
    if e>=16:
        e-=16
        r+=10000
    if e>=8:
        e-=8
        r+=1000
    if e>=4:
        e-=4
        r+=100
    if e>=2:
        e-=2
        r+=10
    if e>=1:
        e-=1
        r+=1
    return r
numero=float(input("Ingrese valor a calcular: "))
print("resultado=",binario(numero))