#Contestador de celular
numTlf=int(input("Ingrese numero telefonico:"))
horaLlamada=int(input("Ingrese hora de la llamada:"))
antes_14=numTlf % 10**3 #909
antes_17_19=numTlf // 10**5 #877
if horaLlamada>=19 : 
        print("NO CONTESTAR")
if horaLlamada>=0 and horaLlamada<=7 and antes_14!=909: 
        print("CONTESTAR")
if  horaLlamada<14 and antes_14==909 : 
            print("CONTESTAR")
if horaLlamada>=17 and horaLlamada<=19 and antes_17_19==877: 
        print("NO CONTESTAR")      