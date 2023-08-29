def numero_perfecto(a):
    i=1
    contador=0
    while i<a:
        division=a%i
        if division!=0:
            contador=contador
        elif division==0:
            contador=contador+i
        i=i+1
    if contador==a:
        return True
    elif contador!=a:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))