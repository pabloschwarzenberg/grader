def amigos(numero1, numero2):
    sum_div_num1 = sum([i for i in range(1, numero1) if numero1 % i == 0])
    sum_div_num2 = sum([i for i in range(1, numero2) if numero2 % i == 0])

    if sum_div_num1 == numero2 and sum_div_num2 == numero1:
        return True
    else:
        return False

if __name__ == "__main__":
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    if amigos(numero1, numero2):
        print("Los números son amigos")
    else:
        print("Los números no son amigos")
