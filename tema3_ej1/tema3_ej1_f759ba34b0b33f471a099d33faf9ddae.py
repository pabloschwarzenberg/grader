def suma_divisores(n):
    divisores = [1]
    for i in range(2, n + 1):
        if n % i == 0:
            divisores.append(i)
            
    return sum(divisores)
resultadosuma = suma_divisores(n)
resultado = resultadosuma

def esprimo(resultado):
    if resultado < 1:
        return False
    elif resultado == 2:
        return True
    else:
        for i in range(2, resultado):
            if resultado % i == 0:
                return False
            return True
if resultado is True:
    print("El numero es primo")
else:
        print("El numero no es primo")
print(resultado)

if __name__ == "__main__":
n = int(input("Ingrese un divisor"))