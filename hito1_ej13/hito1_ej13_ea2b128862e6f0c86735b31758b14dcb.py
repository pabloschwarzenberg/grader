#Factores Primos
y=0
modulo_base=2

n=int(input("Ingrese un numero: "))

while(n!=1):
    if(n<0):
        if(n%modulo_base==0):
            paso1=str(modulo_base)
            print("-%d"%modulo_base)
            n=n/modulo_base
        else:
            modulo_base= modulo_base+1
    elif(n%modulo_base==0):
        paso1=str(modulo_base)
        print(modulo_base)
        n=n/modulo_base
    else:
        modulo_base= modulo_base+1



