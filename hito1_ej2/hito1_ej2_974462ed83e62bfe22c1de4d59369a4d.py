# valores
number = str(input("Ingrese el número telefónico: "))
hour = int(input("Ingrese la hora de la llamada: "))

# condicionales
# .. . . _  .

if (0 <= hour <= 7):
    print("CONTESTAR! WAKE UP")

elif (14 <= hour <= 16):
    print("NO CONTESTAR")
elif (8 <= hour <= 14 ):
    if str(number[-3]) == "9" and str(number[-2]) == "0" and str(number[-1]) == "9":
        print("CONTESTAR! WAKE UP")
    else:
        print("NO CONTESTAR")


elif (hour >= 17 <= 19):
    if str(number[-3]) == "8" and str(number[-2]) == "7" and str(number[-1]) == "7":
        print("CONTESTAR! WAKE UP")
    else:
        print("NO CONTESTAR")

elif(20 <= hour):
    print ("NO CONTESTAR")

else:
    print("NO CONTESTAR")

