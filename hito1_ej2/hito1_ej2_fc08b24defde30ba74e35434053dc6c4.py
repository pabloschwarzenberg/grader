#Contestador de celular
numero =(input("Ingrese numero telefonico: "))

hora = int(input("Ingrese la hora de la llamada: "))

ultimosnumeros = numero[-3:]
primerosnumeros = numero[:3]

if (hora > 0 and hora <= 7):
    print("Contestar")  

elif (hora > 7 and hora < 14 ):
    if ultimosnumeros == "909":
        print("Contestar")
    else:
        print("No contestar")
elif (hora > 17 and hora < 19):
    if primerosnumeros == "877":
        print("No contestar")
    else:
        print("Contestar")
elif (hora > 19):
      print("No contestar")    
      