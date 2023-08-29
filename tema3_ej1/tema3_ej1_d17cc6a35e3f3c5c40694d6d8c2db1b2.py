# completa el código de la función
def suma_divisores(numero):
    divisores = [i for i in range(1, numero) if numero % i == 0]
    suma = sum(divisores)
    es_primo = suma == 1
    return suma, es_primo

# Ejemplo de uso de la función
numero = int(input("Ingrese un número: "))
resultado, es_primo = suma_divisores(numero)

print(f"La suma de los divisores de {numero} es: {resultado}")
print(f"El número {numero} {'es primo' if es_primo else 'no es primo'}")
