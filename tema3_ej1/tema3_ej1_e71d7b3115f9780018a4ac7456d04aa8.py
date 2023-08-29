def suma_divisores(a):
    listadivisores = []
    for x in range(1,a+1):
        resto1 = a%x
        if resto1 == 0 and x!=a:
            listadivisores.append(x)
    suma = sum(listadivisores)
    if suma == 1:
        return suma,True
    else:
        return suma,False
    
if __name__ == "__main__":
    a = int(input("Ingrese un número: "))
    if suma_divisores(a):
        print(suma_divisores(a))
    else:
        print(suma_divisores(a))