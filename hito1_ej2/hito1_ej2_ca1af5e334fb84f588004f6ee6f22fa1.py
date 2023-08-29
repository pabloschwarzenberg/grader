n = str(input("Ingrese el número telefonico: "))
h= int(input("Ingrese la hora de la llamada: "))
N = ("Resultado: NO CONTESTAR")
C= ("Resultado: CONTESTAR")
if h>=0 and h<=7:
    print (C)
if h<14 and ("909") in n:
    print (C)
else:
    print (N)
if h>=17 and h<=19 and ("877")in n:
    print (N)
else:
    h>=17 and h<=19
    print (C)
if h>19:
    print (N)
