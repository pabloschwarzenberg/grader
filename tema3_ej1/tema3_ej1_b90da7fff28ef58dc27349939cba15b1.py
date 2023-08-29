# completa el código de la función
def suma_divisores(a):
    B = 0
    for i in range(1, a):
        if a % i == 0:
            B += i
    if B == 1:
        c=True
    if B != 1:
        c=False
    return (B,c)