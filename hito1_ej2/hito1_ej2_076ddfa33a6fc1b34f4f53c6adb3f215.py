#Contestador de celular
numero =(input("Ingrese numero telefonico: "))

hora = int(input("Ingrese la hora de la llamada: "))

ultimos_numeros = numero[-3:]
primeros_numeros = numero[:3]

if (hora > 0 and hora <= 7):
    print("Contestar")  

elif (hora > 7 and hora < 14 ):
    if ultimos_numeros == "909":
        print("Contestar")
    else:
        print("No contestar")
elif (hora > 17 and hora < 19):
    if primeros_numeros == "877":
        print("No contestar")
    else:
        print("Contestar")
elif (hora > 19):
      print("No contestar")
