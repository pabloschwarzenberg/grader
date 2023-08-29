def numero_perfecto(a):
    enteros = list(range(a+1))
    enteros_1 = enteros[1:a]
    divisores = []
    for divisor in enteros_1:
        resto = a % int(divisor)
        if resto == 0:
            divisores.append(divisor)
    suma = 0
    for sumando in divisores:
        suma = suma + int(sumando)
    if suma == a :
        return True
    else :
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           