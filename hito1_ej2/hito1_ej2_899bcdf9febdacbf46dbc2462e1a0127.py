#Contestador de celular
telefono=[]
telefonoalista=str(input("Ingrese numero de telefonico:"))
telefono.append(telefonoalista)
hora=int(input("Ingrese hora de llamada:"))

telefono[0]
if 0<=hora<=7:
    print("CONTESTAR")
if 7<hora<=14:
    if (telefono[0][5]=="9",telefono[0][6]=="0",telefono[0][7]=="9"):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if 17<=hora<=19:
    if (telefono[0][0]=="8",telefono[0][1]=="7",telefono[0][2]=="7"):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if hora>19:
    print("NO CONTESTAR")