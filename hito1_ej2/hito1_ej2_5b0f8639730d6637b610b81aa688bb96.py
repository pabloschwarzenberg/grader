
telefono= (input("Ingrese numero telefonico: "))
hora= int(input("Ingrese hora de la llamada: "))

if 0 <= hora <= 7:
    print("CONTESTAR")
elif 7<hora <14 and (telefono[5:8] == "909"):
    print("CONTESTAR")
elif 7<hora <14: 
    print("NO CONTESTAR")    
elif 14<= hora <17: 
    print("NO CONTESTAR")        
elif 17<= hora <19 and (telefono[0:3] == "877"):
    print("NO CONTESTAR")
elif 17<= hora <19:
    print("CONTESTAR")
elif 19< hora < 24:
    print("NO CONTESTAR")  