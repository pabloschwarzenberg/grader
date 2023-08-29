#Contestador de celular
      
N= int(input("Ingrese número de telefono: "))
H= int(input("Ingrese hora de llamada: "))

centena = N%1000

n=str(N)

pt = n[0:3]


if H>=0 and H<=7:
    print("CONTESTAR")


elif H>7 and H<=14 and N%1000==909:
    print("CONTESTAR")

elif H>7 and H<=14:
    print("NO CONTESTAR")


elif H>=17 and H<=19 and pt=="877":
    print("NO CONTESTAR")

elif H>=17 and H<=19:
    print("CONTESTAR")

elif H>19 and H<23:
    print("NO CONTESTAR")