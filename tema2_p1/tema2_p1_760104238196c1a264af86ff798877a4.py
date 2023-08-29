# por favor escribe aquí tu función
def es_primo(number):

    n = int((number ** (1 / 2)) // 1) + 1
    if number == 1:
        prime = False
    else:
        prime = True
        for var in range(2, n):
            if number / var == number // var:
                prime = False
                break
    return prime
