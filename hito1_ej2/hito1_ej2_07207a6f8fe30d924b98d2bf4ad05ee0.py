#Contestador de celular
numero =(input("Ingrese numero telefonico: "))

hora = int(input("Ingrese la hora de la llamada: "))

ultimodigitos = numero[-3:]
primerodigitos = numero[:3]

if (hora > 0 and hora <= 7):
    print("CONTESTAR")  

elif (hora > 7 and hora < 14 ):
    if ultimodigitos == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif (hora > 17 and hora < 19):
    if primerodigitos == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif (hora > 19):
      print("NO CONTESTAR")
