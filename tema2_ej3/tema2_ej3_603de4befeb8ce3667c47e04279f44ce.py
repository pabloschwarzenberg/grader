def numero_perfecto(a):
    num = False
    suma = 0
    for i in range(a):
        if i == 0:
            continue
        elif a % i == 0:
            suma = suma + i
    if suma == a:
        num = True
    return num
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           