#Contestador de celular
N=int(input("Ingrese el número telefónico de 8 dígitos:"))
H=int(input("Ingrese hora de la llamada:"))
if H>=00.00 and H<=07.00:
    print("CONTESTAR")
if H>07.00 and H<14.00:
    if N-(N-909)==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if H>=14.00 and H<17.00:
   print("NO CONTESTAR")
if H>=17.00 and H<=19.00:
    if N>=87700000 and N<=87799999:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if H>19.00:
   print("NO CONTESTAR")