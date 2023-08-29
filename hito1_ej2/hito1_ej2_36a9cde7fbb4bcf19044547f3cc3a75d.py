#Contestador de celular
#Contestador de celular
numtel = int(input("Ingrese numero telefonico: "))
horallam = int(input("Ingrese hora de llamada: ")) 
numtel1 = str(numtel)[5:8]
numtel2 = str(numtel)[0:3]

if horallam >= 00 and horallam <= 7 :
        print ("Resultado : CONTESTAR")

elif numtel1 == "909" and horallam <= 14:
    print ("Resultado : CONTESTAR")

elif horallam >= 17 and horallam <= 19 and numtel2 =="877":
    print ("Resultado : NO CONTESTAR")

elif horallam >= 19 :
    print ("NO CONTESTAR")    
else: 
    print ("NO CONTESTAR")