# completa el código de la función
def son_amigos(a, b):
    sum_div_a = sum(divisores(a))
    sum_div_b = sum(divisores(b))

    if sum_div_a == b and sum_div_b == a:
        return True
    else:
        return False

def divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

# Ejemplo de uso
print(son_amigos(1, 2))





        