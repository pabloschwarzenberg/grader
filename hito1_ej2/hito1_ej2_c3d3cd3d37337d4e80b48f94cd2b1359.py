numero = int(input("Ingrese su numero telefonico de 8 digistos"))
hora = int(input("Ingrese la hora de su llamada"))
if hora>=0 or hora<=7:
 print("CONTESTAR")
if hora<14:
 if numero ==77389909:
   print("CONTESTAR")
 else:
   print("NO CONTESTAR")
if hora>17 or hora<19:
 if numero == 87765545:
   print("NO CONTESTAR")
 else:
    print("CONTESTAR")
if hora>19:
 print("NO CONTESTAR")