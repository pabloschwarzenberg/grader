n = str(input("Ingrese el número telefónico: "))
h = eval(input("Ingrese hora de la llamada: "))
#str representa texto/cadena de caracteres
if (h >= 0) and (h <= 7):
    print("CONTESTAR")
elif (h >= 19) and (h <=23):
    print("NO CONTESTAR")
elif (h >= 7) and (h <= 14):
    if str(n[-3]) == "9" and str(n[-2]) == "0" and str(n[-1]) == "9":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif (h >= 17) and (h <= 19):
    if str(n[-8]) == "8" and str(n[-7]) == "7" and str(n[-6]) == "7":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")