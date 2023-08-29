# completa el código de la función
def suma_divisores(a):
    x= 1
    suma = 0
    while x < a:
        if a % x == 0:
            suma = suma + x 
        x = x + 1
        return suma

def numeroPrimo(a):
    numero = suma_divisores(a)
    if numero == 1:
        return False
    elif numero ==2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                 return False
        return True

def main():
    a = input("Ingrese el numero: ")
    resultado = (suma_divisores, numeroPrimo)
    print(resultado)
   

if __name__ == "__main__":
    main()