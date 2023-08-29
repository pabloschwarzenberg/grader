#Contestador de celular
 #Contestador de celular
#12345678
#01234567

numero_telefonico = int(input("Ingrese su numero telefonico : "))
hora_llamada = int(input("Ingrese la hora de la llamada : "))
if hora_llamada >=0 or hora_llamada <=7:
    print(" NO CONTESTAR")
elif hora_llamada<14:
  print("NO CONTESTAR")
  if numero_telefonico[0]==9 and numero_telefonico[1]==0 and numero_telefonico [2]==9:
        print(" NO CONTESTAR")
elif hora_llamada>=17 or hora_llamada <=19:
    print(" NOCONTESTAR")
    if numero_telefonico[0]==7 and numero_telefonico[1]==7 and numero_telefonico[2]==8:
        print("NO CONTESTAR")
elif hora_llamada>=17 or hora_llamada<=19:
    print(" NO CONTESTAR")
elif hora_llamada >19:
    print("NO CONTESTAR")    