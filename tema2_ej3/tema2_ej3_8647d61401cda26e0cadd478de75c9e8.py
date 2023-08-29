def numero_perfecto(a):
    valor = 0
    for i in range(1,a):
        if a %i == 0:
            valor += i
    if a == valor:
            return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))

