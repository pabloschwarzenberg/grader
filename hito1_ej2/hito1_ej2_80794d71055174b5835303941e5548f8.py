#Contestador de celular
numero=int(input("ingrese el numero telefonico:"))
hora=int(input("ingrese hora de llamada:"))
A=numero%1000
B=numero//100000
if  hora>=0  and hora<=7:
 print("CONTESTAR")
elif hora>7 and hora<14:
 if A==909:
   print("CONTESTAR")
 else:
    print("NO CONTESTAR")
elif hora>15 and hora<17:
   print("NO CONTESTAR")
elif hora>=17 and hora<19:
    if B==877:
      print("NO CONTESTAR")
elif hora>=19:
    print("NO CONTESTAR")