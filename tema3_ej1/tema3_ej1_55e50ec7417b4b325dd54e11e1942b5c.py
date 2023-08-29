# completa el código de la función
def suma_divisores(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return sum(divisores)

def es_primo(resultado):
    if resultado == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    n = int(input("Ingrese un numero: "))
    resultado = suma_divisores(n)
    b = es_primo(resultado) 
    print(str(resultado)+ str(", ") + str(b))