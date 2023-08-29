#Contestador de celular
NTEL=(int(input("ingrese el numero telefonico: ")))
HLLA=(int(input("Ingrese la hora de llamada: ")))
SNTEL=str(NTEL)
SHLLA=str(HLLA)
x=0
while(x<1):
 if(len(SNTEL)==8):
      x=x=1
      print()
 elif(len(SNTEL)>8):
        print("valor valido")
for i in range(0,23):
  if(HLLA<=0 and HLLA<7):
   print("Contestar ya que podría ser una emergencia")
  elif(HLLA<14 and SNTEL[5]=="9"and SNTEL[6]=="0"and SNTEL[7]=="9"):
   print("Contestar")
  elif(HLLA>=17 and HLLA<=19):
   print("No Contestar")
   if(SNTEL[0]=="8"and SNTEL[1]=="7"and SNTEL[2]=="7"):
    print("No Contestar")
   else:()
   print("Contestar")
  elif(HLLA>19):
        print("No Contestar")