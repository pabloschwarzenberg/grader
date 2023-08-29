#Contestador de celular
N=str(input("Ingrese numero telefonico:"))
hr=int(input("Ingrese hora de la llamada:"))
LAST=N[5:8]
LAST=eval(LAST)
COM=N[0:3]
COM=eval(COM)
if hr>23:
  print("marque una hora entre las 00 y 23 hrs")
if LAST==909 and hr<14 or 0<=hr<=7 or 17<hr<19 and COM!=877:
  print("CONTESTAR")
elif hr>19 or COM==877:
  print("NO CONTESTAR")
    
    
