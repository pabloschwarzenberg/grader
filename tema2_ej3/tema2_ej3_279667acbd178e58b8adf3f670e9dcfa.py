def numero_perfecto(a):
    numeros = 0
    for x in range(1,a):
        if a % x == 0:
            numeros += x
    if numeros == a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))