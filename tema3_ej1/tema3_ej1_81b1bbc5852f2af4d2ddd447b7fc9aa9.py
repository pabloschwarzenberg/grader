# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    
    if suma == 1:
        return suma, True  
    else:
        return suma, False 


if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    suma, es_primo = suma_divisores(numero)
    print("La suma de los divisores de", numero, "es:", suma)
    if es_primo:
        print(numero, "es un número primo.")
    else:
        print(numero, "no es un número primo.")
  
           