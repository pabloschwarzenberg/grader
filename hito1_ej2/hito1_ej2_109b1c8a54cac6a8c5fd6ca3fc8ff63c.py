#Hito 1 contestador
numero=input("Ingrese numero telefonico ")
dig1=(int(numero[0]))
dig2=(int(numero[1]))
dig3=(int(numero[2]))
dig6=(int(numero[5]))
dig7=(int(numero[6]))
dig8=(int(numero[7]))
hora=int(input("Ingrese hora de la llamda "))
if (hora) >=0 and (hora) <=7:
         print("CONTESTAR")
elif (hora) <=14 and dig6==9 and dig7==0 and dig8==9:
         print("CONTESTAR")
elif (hora) >=17 and hora <=19 and dig1!=8 and dig2!=7 and dig3!=7:
         print("CONTESTAR")
else:
         print("NO CONTESTAR")


