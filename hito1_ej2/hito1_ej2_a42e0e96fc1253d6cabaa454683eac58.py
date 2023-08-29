#Contestador de celular
numero=int(input("ingrese numero telefonico= "))
hora=int(input("ingrese hora de la llamada= "))

a=numero%1000
b=numero/100000

if hora>=0 and hora<=7:
         print("CONTESTAR")
elif hora>7 and hora<14  and a==909:
         print("CONTESTAR")
elif hora>=17 and hora<=19 and int(b)!=877:
         print("CONTESTAR")
else:
         print("NO CONTESTAR")

      