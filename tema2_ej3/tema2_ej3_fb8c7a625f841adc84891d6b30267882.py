def numero_perfecto(a):
    contador = 1
    suma = 0
    while contador!= a:
        if a%contador == 0:
            suma = suma + contador
        contador = contador + 1
    if suma==a:
        return True
    else:
        return False

if __name__=="main_":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))