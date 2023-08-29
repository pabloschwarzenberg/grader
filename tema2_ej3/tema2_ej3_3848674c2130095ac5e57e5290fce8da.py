def numero_perfecto(a):
    sumador=0
    for i in range (1,a):
        if a%i == 0:
            sumador=sumador+i
    if sumador == a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           