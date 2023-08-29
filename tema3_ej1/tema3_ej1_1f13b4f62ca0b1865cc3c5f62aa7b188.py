# completa el codigo de la funcion
def suma_divisores(a):

    suma = 0
    primo = False
    for i in range(1, a): 

        if (a % i) == 0: 
            suma = suma + i

    else: 
        if suma == 1: 
            primo = True

    return suma, primo            






if __name__ == "__main__":

    print(
    suma_divisores(1),
    suma_divisores(8),
    suma_divisores(13)
    )       




           