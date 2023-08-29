def mcm(a,b,ab):
    if b==0:
        return 0
    return (ab)/min(b,a%b)

if __name__=="__main__":
    a=int(input("Ingrese el primer número: "))
    b=int(input("Ingrese el segundo número: "))
    ab=a*b
    print("El mínimo común múltiplo es: ",mcm(a,b,ab)) 