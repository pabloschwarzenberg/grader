# completa el código de la función

def divisores(numero):
    if numero <= 0:
        print("¡Le he pedido un número entero mayor que cero!")
    else:
        sumadiv= 0
        for i in range(1, numero):
            if numero % i == 0:
                sumadiv= sumadiv+i
    return sumadiv

def amigos(numero1,numero2):
    a= divisores(numero1)
    b= divisores(numero2)
    if a==numero2 and b==numero1:
        print("Son numeros amigos")
        return True
    else:
        print("No son numeros amigos")
        return False
if __name__ == "__main__":
    numero1= int(input("Ingrese el primer numero"))
    numero2= int(input("Ingrese el segundo numero"))
    print(amigos(numero1, numero2))