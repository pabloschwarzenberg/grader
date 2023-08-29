#Contestador de celular
      numero = input("ingrese numero telefonico: ")
      hora = int(input("ingrese hora de la llamada: "))
if hora >= 0 and hora <= 7:
      print("contestar")
elif hora < 14:
    if numero[-3:]=="909":
    print("contestar")
    else: 
       print("no contestar")
elif hora >= 17 and hora <=19:
       if numero[:3]=="877":
           print("no contestar")
           else:
              print("contestar")
               if hora >= 19:
                  print("no contestar")
              
          