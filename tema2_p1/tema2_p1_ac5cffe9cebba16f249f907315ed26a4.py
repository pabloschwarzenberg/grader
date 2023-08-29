def numb():
    num = int(input("Ingrese su numero: "))
    resultado = es_primo(num) 

    if resultado is True:
        print("True")
    else:
        print("False")

def es_primo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for n in range(2, num):
            if num % n == 0:
                return False
        return True

num = int(input("Ingrese su numero: "))
        for n in range(2, num):
            if num % n == 0:
                return False
        return True