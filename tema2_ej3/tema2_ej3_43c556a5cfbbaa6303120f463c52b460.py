def numero_perfecto(a):
    suma = 0
    g = []
    for i in range(1,a):
        if a%i == 0:
            g.append(i)
    print(g)
    for o in g:
        suma = suma + int(o)

    if suma == a:
        return True

    elif suma != a:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           