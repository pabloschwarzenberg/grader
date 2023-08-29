#Contestador de celular
n = input("Ingrese numero telefonico: ")
h = int(input("ingrese hora de la llamada: "))

if(len(n) == 8 and h <= 23 and h >= 0):
    if(h >= 0 and h <= 7):
        print("CONTESTAR")

    elif(h < 14  or n[len(n)-3] == "909"):
        print("CONTESTAR")  
    elif(h >= 17  and h <= 19 and n[0:3] != "877"):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")