def es_primo(n):
    if n <=1:
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
    return True

try:
    n = int(input("Ingrese un numero, o ingrese 0 para salir: "))
    if n == 0:
            print("Su numero debe ser distinto de 0")
    if es_primo(n):
            print("Su numero %s es primo" % n)
    else:
            print("Su numero %s no es primo" % n)
except:
        print("El numero tiene que ser entero")