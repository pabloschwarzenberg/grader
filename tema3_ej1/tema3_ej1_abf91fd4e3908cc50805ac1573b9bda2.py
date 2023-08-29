# completa el código de la función

def suma_divisores(x):

    h = 0

    for a in range (1,x):

        if x%a == 0:

            h+=a

    if h == 1:

        return h, True

    else:

        return h, False


           
if __name__ == "__main__":
    pass