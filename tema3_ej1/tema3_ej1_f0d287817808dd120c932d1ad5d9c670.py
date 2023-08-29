# completa el código de la función
if __name__ == "__main__":
    print("Dame un numero: ")
    input1 = input()
    entrada = int(input1)

def suma_divisores(a):
    suma = 0
    for i in range(1, a):
        if a%i == 0:
            suma = suma + i    
    if suma == 1 :
        return(suma,True)
    return(suma,False)


if __name__ == "__main__":
    resultado, es_primo = suma_divisores(entrada)
    print("La suma de los divisores es: ", resultado)
    if es_primo:
        print("El numero es primo")
        print(entrada)    



