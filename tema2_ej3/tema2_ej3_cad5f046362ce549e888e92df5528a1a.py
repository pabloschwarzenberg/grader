# Declaración de la función
def numero_perfecto(n):
    sd = 0
    for i in range(1,n):
        if (n%i==0):
            sd = sd + i
    if sd==n:
        return True
    else:
        return False

