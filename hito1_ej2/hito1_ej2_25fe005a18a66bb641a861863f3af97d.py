#Contestador de celular
NT=(input("ingrese número de teléfono: "))
if len(NT)>8:
    print("número",NT, " invalido, ingrese otro número")
HLL= int(input("ingrese hora de llamada"))
if HLL>=0 and HLL<=7:
    print("contestar")
elif HLL<14:
    if NT[-1]=='9' and NT[-2]=='0' and NT[-3]=='9':
        print("contestar")
    else:
        print("no contestar")
elif HLL>=17 and HLL<=19:
    if NT[0]=='8' and NT[1]=='7' and NT[2]=='7':
        print("no contestar")
elif HLL>19:
    print("no contestar")
