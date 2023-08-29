# completa el código de la función
def suma_divisores(a):

    divisores = [0]

    for i in range(1, a):

        if a % i == 0:
            divisores.append(i)
           
    suma_total = sum(divisores)
    if suma_total == 1:
        return suma_total, True
    
    else:
        return suma_total, False

if __name__ == "__main__":

    a = eval(input("Ingrese número: "))

    resultado = suma_divisores(a)

    print(resultado)