#Contestador de celular
result = ""
Nrofono = int(input("Ingrese numero telefonico: "))
Horall = int(input("Ingrese hora de la llamada: "))

if len(str(Nrofono)) == 8:
    if Horall >= 0 and Horall <= 23:

        #Logica
        if Horall >= 0 and Horall <= 7:
            result = "CONTESTAR"
        elif Horall > 7 and Horall < 14:
            if (Nrofono % 1000) == 909:
                result = "CONTESTAR"
            else:
                result = "NO CONTESTAR"
        elif Horall >= 15 and Horall <= 19:
            if (Nrofono // 100000) == 877:
                result = "NO CONTESTAR"
            else: 
                result = "CONTESTAR"
        else:
            result = "NO CONTESTAR"


print("Resultado:", result)   