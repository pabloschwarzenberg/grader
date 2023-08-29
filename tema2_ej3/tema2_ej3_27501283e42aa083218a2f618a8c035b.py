def numero_perfecto(a):
    x = a - 1
    resultado = 0
    while x > 0:
        if a % x == 0:
            resultado += x
        x = x - 1
    if resultado != a:
        return(False)
    else:
        return(True)


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           