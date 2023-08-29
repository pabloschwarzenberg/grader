#Contestador de celular
nTel = int(input("Ingrese el numero telefonico: "))
HL = eval(input("Ingrese la hora de la llamada (0 o 23): "))

nTel = str(nTel)

if HL >= 0 and HL <= 7:
    print("CONTESTAR")
    
if HL > 7 and HL <= 14:
    if nTel[5:] == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
        
if HL >= 17 and HL <= 19:
    if nTel[0:3] == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
        
if HL >= 19 and HL < 24:
    print("NO CONTESTAR")    