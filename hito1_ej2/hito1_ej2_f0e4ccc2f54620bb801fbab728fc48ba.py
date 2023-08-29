#Contestador de celular
N=int(input("Ingrese el numero telefonico: "))
minH=0
maxH=23
H=int(input("Ingrese hora de la llamada: "))

if (H<=7):
  print("CONTESTAR") 
  
if (7<H<=14):
  if (N % 1000==909):  
    print("CONTESTAR")
  else: print("NO CONTESTAR")
  
if (14<H<17):
  print("NO CONTESTAR")
  
if (17<=H<=19):
  if (N % 1000==545):
    print ("NO CONTESTAR")
  else: print ("CONTESTAR")

if (19<H):
  print("NO CONTESTAR")