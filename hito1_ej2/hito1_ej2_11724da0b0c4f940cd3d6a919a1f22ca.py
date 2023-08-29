#Contestador de celular
N=int(input("Ingrese el numero telefonico -> "))
H=int(input("ingrese la hora de la llamada ->  "))
if H>=24 or H<0:
    print("La hora debe ser entre 0 y 24, intentelo denuevo")
elif N<=10000000 or N>=99999999:
    print("El telefono debe tener 8 digitos, intentelo denuevo")
else:
    U=N%1000
    P=N*1000
    if H>19:
        print("NO CONTESTAR")
    elif  H>0 and H<7:
        print("CONTESTAR")
    elif H>7 and H<14 and U==909:
       print("CONTESTAR")
    elif H>17 and H<19 and P==877:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")