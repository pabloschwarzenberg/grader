# completa el código de la función
def suma_divisores(a):
    b = 0
    for x in range(1,a):
        if a%x == 0:
            b = b + x
    if a == 1:
        return "0, False"
    if b == 1:
        return str(b)+", True"
    else:
        return str(b)+", False

if __name__ == "__main__":
   suma_divisores()





           