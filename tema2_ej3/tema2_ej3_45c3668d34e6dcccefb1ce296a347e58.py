def numero_perfecto(s):
    suma=0
    for m in range(1,s):
        if s%m==0:
            suma=suma+m
    if suma==s:
        return (True)
    else:
        return (False)

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
