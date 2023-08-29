while True:
    try:
        nmin=int(input("Introduzca su numero minimo del rango a calcular: "))
        break
    except ValueError:
        print("Debe ser un numero, no una letra")
while True:
    try:
        nmax=int(input("Introduzca su numero maximo del rango a calcular: "))
        break
    except ValueError:
        print("Debe ser un numero, no una letra")
while nmin<=nmax:
    if (nmin%2==0 or nmin%7==0):
        print(nmin)
    nmin+=1
print("Ha terminado el proceso")