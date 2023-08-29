#Factores Primposible
x=int(2)
numero=int(input("ingrese un numero mayor a 1:"))
while(numero!=1):
    if (numero%x==0):
        print("[",str(x) + "",end="]")
        numero=numero/x
    else:
        x=x+1