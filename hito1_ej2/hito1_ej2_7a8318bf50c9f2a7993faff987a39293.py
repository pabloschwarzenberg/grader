#Contestador de celular
num=int(input("Ingrese el número telefónico (8 cifras): "))
hor=int(input("Ingrese hora de la llamada (entre 0 y 23): "))
if hor in range(7):
    print("CONTESTAR")
elif hor in range(8,14):
    if num%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hor in range(17,19):
    if num//100000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
 