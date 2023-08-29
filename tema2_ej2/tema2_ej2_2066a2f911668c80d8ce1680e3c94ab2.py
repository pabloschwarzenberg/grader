# completa el código de la función

def amigos(a, b):
    def Divisores(numero):
        contador = 0
        for i in range(1, numero):
            if numero % i == 0:
                contador += i
        return contador
    
    contador_a = Divisores(a)
    contador_b = Divisores(b)
    
    if contador_a == b and contador_b == a:
        return True
    else:
        return False

def main():
    a = int(input("Ingrese número A: "))
    b = int(input("Ingrese número B: "))
    print(amigos(a, b))
    
if __name__ == "__main__":
    main()
