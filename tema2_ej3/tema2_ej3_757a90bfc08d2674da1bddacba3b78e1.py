def numero_perfecto(a):
    divisores=[]
    suma=0
    for d in range(1,a):
        if a % d==0:
            divisores.append(d)
    for q in divisores:
        if q == a:
            divisores.remove(q)
    for s in divisores:
        suma += s
    if suma == a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           