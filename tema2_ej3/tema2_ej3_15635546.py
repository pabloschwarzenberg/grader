def numero_perfecto(a):
    numero_perfecto = False
    suma = 0
    for i in range (1,a):
        if a % i == 0:
            suma = suma + i
    if suma == a:
        numero_perfecto = True
    return numero_perfecto

if __name__=="__main__":
    suma_np=0
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
    for i in range (1,a):
        if numero_perfecto(i)==True:
            suma_np= suma_np + i
    print(suma_np)


           