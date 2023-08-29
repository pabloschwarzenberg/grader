#Contestador de celular
ntelefono = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))
if hora in range (0,8):
    print("CONTESTAR")
elif hora in range (8,15) and ntelefono%1000==909:
    print("CONTESTAR")
elif hora in range (8,15):
    print("NO CONTESTAR")
elif hora in range (17,20) and ntelefono//100000==877:
    print("NO CONTESTAR")
elif hora in range (17,20):
    print("CONTESTAR")
elif hora in range (19,24):
    print("NO CONTESTAR")
          
      