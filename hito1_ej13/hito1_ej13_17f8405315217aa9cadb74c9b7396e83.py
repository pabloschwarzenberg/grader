#Factores Primos
x = int(2) 
numeroP = int(input("Ingrese el numero: ")) 
while(numeroP != 1): 
  if (numeroP % x == 0 ):
    print(str(x) + "") 
    numeroP = numeroP / x 
  else:
    x = x + 1


# suma de los divisores de un numero

def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    
    if suma == 1:
        return suma, True  # Retorna la suma y True si el número es primo
    else:
        return suma, False  # Retorna la suma y False si el número no es primo

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    suma, es_primo = suma_divisores(numero)
    print("Suma de los divisores:", suma)
    print("¿Es primo?", es_primo)      