# completa el código de la función
def suma_divisores(a):
    suma_divi = 0
    for n in range(1,a):
        if a % n == 0:
            suma_divi += n
    print("La suma de los divisores es :", suma_divi)

    
    if suma_divi == 1:
        print("El numero es primo")
        return suma_divi, True
    else:
        print("El numero no es primo")
        return suma_divi, False
    

if __name__ == "__main__":
    a = int(input("Ingrese un numero: "))   
    print(suma_divisores(a))