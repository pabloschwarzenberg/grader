#Contestador de celular
telefono=input("ingrese numero telefonico:")
numStr=telefono
len(numStr)==8
final=numStr[5]+numStr[6]+numStr[7]
inicio=numStr[0]+numStr[1]+numStr[2]
hora=int(input("ingrese hora de llamada:"))
if hora <=7 and hora >=0:
     print("contestar")
if hora <14:
     if final=="909":
           print("contestar")
     else:
          print("no contestar")
if hora <=19 and hora >=17:
     if inicio=="877":
           print("no contestar")
     else:
          print("contestar")
if hora >19:
     print("no contestar")
      