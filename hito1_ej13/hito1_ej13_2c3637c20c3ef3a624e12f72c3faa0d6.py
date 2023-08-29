#Factores Primos
x=2
numero=int(input("ingrese el numero: "))
while (numero!=1):
    if numero%x==0:
        print(str(x)+"")
        numero=numero/x
    else:
        x+=1    