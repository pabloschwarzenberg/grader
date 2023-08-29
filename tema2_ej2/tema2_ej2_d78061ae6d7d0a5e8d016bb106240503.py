# completa el código de la función
def son_amigos(a, b):
    sum_a = sum_divisores(a)
    sum_b = sum_divisores(b)

    if sum_a == b and sum_b == a:
        return True
    else:
        return False


def sum_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma
    
if __name__ == "__main__":
    a = 220
    b = 284
    if son_amigos(a, b):
        print(str(a) + " y " + str(b) + " son números amigos.")
    else:
        print(str(a) + " y " + str(b) + " no son números amigos.")
