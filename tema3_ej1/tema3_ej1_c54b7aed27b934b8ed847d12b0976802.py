# completa el código de la función
def suma_divisores(a):
    div = 1
    suma = 0
    vf = a
    while div < a:
        if a % div == 0:
            suma = suma + div
        div = div + 1
    if suma == 1:
        vf=True
    else:
        vf=False
    return (suma,vf)
           