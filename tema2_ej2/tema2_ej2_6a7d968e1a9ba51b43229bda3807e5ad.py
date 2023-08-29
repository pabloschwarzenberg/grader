# completa el código de la función
def amigos(a,b):
    suma=1
    sumb=1
    for n in range(2, a):
        if a % n == 0:
            suma= suma + n
    for n in range(2, b):
        if b % n == 0:
            sumb= sumb + n
    if a == sumb and b == suma:
        return True
    return False