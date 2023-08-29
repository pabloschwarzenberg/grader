#Contestador de celular
nm = str(input("Ingrese el numero telefonico: "))
tm = int(input("Ingrese la hora del llamado: "))
m = nm[5:9]
n = nm[0:3]
int(m)
int(n)
if (tm >= 0) and (tm <= 19) :
   if (tm >= 0) and (tm <= 7) :
    print("CONTESTAR")
   elif (tm >= 7) and (tm <= 14):
    if (m=="909"):
     print("CONTESTAR")
    else:
     print("NO CONTESTAR")
   elif (tm >= 17) and (tm <= 19):
    if(n =="877"):
     print("NO CONTESTAR")
   else:
     print("CONTESTAR")
else:
 print("NO CONTESTAR")