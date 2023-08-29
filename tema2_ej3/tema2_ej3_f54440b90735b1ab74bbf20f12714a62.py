def numero_perfecto(a):
    suma_divisores = 0
    for n in range(1,a):
        if a % n == 0:
            suma_divisores += n
    
    if suma_divisores == a:
        print("Es un numero perfecto")
        return True
    else:
        print("No es un numero perfecto")
        return False

if __name__ == "__main__":
    a = int(input("Ingrese un numero: "))
    print(numero_perfecto(a))