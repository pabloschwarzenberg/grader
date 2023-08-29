#Contestador de celular
n = int(input("Número telefónico: "))
h = int(input("Hora de la llamada: "))
n = str(n)
if len(n) == 8:
    if h >= 0 and h <= 7:
        print("CONTESTAR")
    elif h > 7 and h <= 14:
        if n.endswith("909"):
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    elif h >= 17 and h <= 19:
        if n.startswith("877"):
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")
    elif h > 19 and h <= 23:
        print("NO CONTESTAR")
    else:
        print("La hora es errónea, por favor ingrese de 0 a 23")
else:
    print("El número telefónico es erróneo. Debe ingresar 8 dígitos.")  