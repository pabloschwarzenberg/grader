#Contestador de celular
numero=str(input("Numero telefonico: "))
hora=int(input("Hora de llamada: "))

if 0<hora<7:
   print("CONTESTAR")
if 7<hora<14 and numero [5:]!="909":
    print("NO CONTESTAR")
if 7<hora<14 and numero [5:]=="909":
    print("CONTESTAR")
if 17<hora<19 and numero [5:]!="877":
    print("NO CONTESTAR")
if 17<hora<19 and numero [5:]=="877":
    print("CONTESTAR")
if 19<hora<24:
    print("NO CONTESTAR")

      