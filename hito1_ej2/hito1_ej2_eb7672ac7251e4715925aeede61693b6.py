#Contestador de celular
numero=str(input("Ingresa número telefónico: "))
hora=int(input("Ingrese Hora de la llamada: "))

if 0<=hora<=7:
    print("CONTESTAR")
if 7<hora<=14 and numero[5:]!="909":
    print("NO CONTESTAR")
if 7<hora<=14 and numero[5:]=="909":
    print("CONTESTAR")
if 17<=hora<=19 and numero[:3]!="877":
    print("CONTESTAR")
if 17<=hora<=19 and numero[:3]=="877":
    print("NO CONTESTAR")
if hora>19:
    print("NO CONTESTAR")

     