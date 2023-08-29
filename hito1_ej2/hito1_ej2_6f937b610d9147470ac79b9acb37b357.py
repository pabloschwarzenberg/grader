#Contestador de celular
NT=int(input("Ingrese número telefonico: "))
HL=int(input("Ingrese hora de la llamada: "))
if 0<=HL>=7:
    print("Resultado: Contestar")
if 7<HL>=14:
    if NT % 1000 == 909:
        print("Resultado: Contestar")
    else:
        print("Resultado: No Contestar")
if 14<HL>=17:
    print("Resultado: No Contestar")
if 17<HL>19:
    if NT//100000 == 877:
        print("Resultado: No Contestar")
    else:
        print("Resultado: Contestar")
if 19<=HL<=23:
    print("Resultado: No Contestar")