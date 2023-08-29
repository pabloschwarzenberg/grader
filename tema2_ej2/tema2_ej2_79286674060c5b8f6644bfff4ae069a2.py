# completa el código de la función
def amigos(num1,num2):
    suma_divisores_a =0
    a = 1
    while a <= num1:
        if num1 % a == 0:
            suma_divisores_a+=a
        else:
            pass
        a += 1

    suma_divisores_b = 0
    b = 1
    while b <= num2:
        if num2 % b == 0:
            suma_divisores_b += b
        else:
            pass
        b += 1
    if suma_divisores_a==suma_divisores_b and num1!=num2:
        return True
    else:
        return False

