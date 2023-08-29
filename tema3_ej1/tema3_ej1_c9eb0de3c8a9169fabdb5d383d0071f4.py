# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    
    if suma == 1:
        es_primo = True
    else:
        es_primo = False
    
    return suma, es_primo

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    resultado = suma_divisores(num)
    if resultado[1]:
        print(num,"es un número primo")
    else:
        print(num,"no es un número primo")