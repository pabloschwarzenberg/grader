#Contestador de celular
N=int(input("Ingrese un numero telefonico: "))
H=int(input("ingrese hora de la llamada:  "))
if (H>=24 or H<0):
    print("hora debe ser entre 0 y 23")
elif (N<=10000000 or N>=99999999):
    print("debe ser un numero de 8 digitos")
else:
    UN=(N%1000)
    if (H>19):
        print("NO CONTESTAR")
    elif  (H>0 and H<7):
        print("CONTESTAR")
    elif (H>7 and H<14 and UN==909):
       print("CONTESTAR")
    elif (H>17 and H<19 and not UN==877):
        print("NO CONTESTAR")
    else:
        print("NO CONTESTAR")     