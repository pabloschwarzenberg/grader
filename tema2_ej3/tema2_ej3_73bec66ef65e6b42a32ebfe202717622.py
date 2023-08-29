def numero_perfecto(a):
    lista=[]
    b=a-1
    while b>0:
        if a%b==0:
            lista.append(b)
            b=b-1
            continue
        else:
            b=b-1
            continue
    sumar=0
    for j in lista:
        sumar=sumar+j
    if sumar==a:
        return True
    elif sumar!=a:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           