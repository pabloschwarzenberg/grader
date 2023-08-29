#Contestador de celular
n = str(input("Ingrese numero telefonico: "))
h = int(input("Ingrese hora de llamada: "))
if h > 0 and h < 7:
    print("CONTESTAR")
elif h > 19 and h <= 23:
    print("NO CONTESTAR")
elif h > 7 and h < 14 and n[-3] == '9' and n[-2] == '0' and n[-1] == '9':
    print("CONTESTAR")
elif h > 7 and h < 14 and n[-3] != '9' and n[-2] != '0' and n[-1] != '9':
    print("NO CONTESTAR")
elif h > 17 and h < 19 and n[0] == '8' and n[1] == '7' and n[2] == '7':
    print("NO CONTESTAR")
elif h > 17 and h < 19 and n[0] != '8' and n[1] != '7' and n[2] != '7':
    print("CONTESTAR")      