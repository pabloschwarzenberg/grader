Number = str(input("Ingrese el número telefónico:"))
Hour = int(input("Ingrese hora de la llamada:"))

if Hour > 0 and Hour < 7:
    print("Contestar")
if Hour > 19 and Hour <= 23:
    print("No contestar")
    
else:
    if Hour > 7 and Hour < 14 and str(Number[-3]) == "9" and str(Number[-2]) == "0" and str(Number[-1]) == "9":
        print("Contestar")
    if Hour > 7 and Hour < 14 and str(Number[-3]) != "9" and str(Number[-2]) != "0" and str(Number[-1]) != "9":
        print("No contestar")
    if Hour > 17 and Hour < 19 and str(Number[0:1]) == "8" and str(Number[1:2]) == "7" and str(Number[2:3]) == "7":
        print("No contestar")
    if Hour > 17 and Hour < 19 and str(Number[0:1]) != "8" and str(Number[1:2]) != "7" and str(Number[2:3]) != "7":
        print("Contestar")