#Contestador de celular
telefono="12345678"
if __name__ == "__main__":
  while len(telefono)!=9:
    telefono=str(input("ingrese numero telefonico : "))
    hora=int(input("ingrese hora de la llamada : "))
    ultimos3=telefono[5:8]
    if hora >=0 and hora <= 7:
        print("CONTESTAR")
    elif hora >0 and hora < 14 and ultimos3== "909":
        print("CONTESTAR")
    elif hora >7 and hora < 23 and ultimos3!= "909":
        print("NO CONTESTAR")
    elif hora >=17 and hora <=19 :
        if ultimos3 == "877":
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")

