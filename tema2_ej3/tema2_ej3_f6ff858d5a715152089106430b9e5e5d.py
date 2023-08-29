def numero_perfecto(a):

    divisores = [0]

    for i in range(1, a):

        if a % i == 0:
            divisores.append(i)
           
    suma_total = sum(divisores)
    if suma_total == a:
        return True
    
    else:
        return False

if __name__ == "__main__":

    a = eval(input("Ingrese número: "))

    resultado = numero_perfecto(a)

    print(resultado)           