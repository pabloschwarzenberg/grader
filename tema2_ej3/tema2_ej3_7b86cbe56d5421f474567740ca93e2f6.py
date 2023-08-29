def numero_perfecto(a):
    suma = []
    for i in range(1, a):
        if a % i == 0:
            suma.append(i)
    suma = sum(suma)
    if suma == a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))