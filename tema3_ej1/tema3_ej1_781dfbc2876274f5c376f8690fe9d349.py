# completa el código de la función
def suma_divisores(a):
    x=a
    divisores_suma=0
    for i in range(x):
        resto=a%x        
        if resto==0:
            divisores_suma+=x
        x-=1
    if x==0:
        if (divisores_suma-a)==1 and a!=1:
            return int(divisores_suma-a), True
        else:
            return int(divisores_suma-a), False
            

if __name__ == "__main__":
    a=int(input("Ingrese un numero:"))
    print(suma_divisores(a))

           