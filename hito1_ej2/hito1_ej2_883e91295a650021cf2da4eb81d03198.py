#Contestador de celular
numTel=int(input("Ingrese número de teléfono: "))
horaLlamada=int(input("Ingrese hora de llamda: "))
antes_14=numTel % 10**3
antes_17_19=numTel // 10**5
if horaLlamada>=19:
    print ("NO CONTESTAR")
if horaLlamada>=0 and horaLlamada<=7 and antes_14!=909:
    print ("CONTESTAR")
if horaLlamada<14 and antes_14==909:
    print ("CONTESTAR")
if horaLlamada>=17 and horaLlamada<=19 and antes_17_19==877:
    print ("NO CONTESTAR")  