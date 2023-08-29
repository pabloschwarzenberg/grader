telephone = int(input("Ingrese numero telefonico: "))
callTime = int(input("Ingrese hora de llamada: ")) 
telephone1 = str(telephone)[5:8]
telephone2 = str(telephone)[0:3]

if callTime >= 00 and callTime <= 7 :
        print ("Resultado: CONTESTAR")

elif telephone1 == "909" and callTime <= 14:
    print ("Resultado: CONTESTAR")

elif callTime >= 17 and callTime <= 19 and telephone2 =="877":
    print ("Resultado: NO CONTESTAR")

elif callTime >= 19 :
    print ("Resultado: NO CONTESTAR")    
else: 
    print ("Resultado: NO CONTESTAR")