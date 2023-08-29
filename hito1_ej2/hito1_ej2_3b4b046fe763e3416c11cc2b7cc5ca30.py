#Contestador de celular
validar_numero=True
validar_hora=True
while validar_numero:
    numero=int(input("numero telefonico:"))
    if numero<100000000 and numero>9999999:
        validar_numero=False
    else:
        print("numero invalido, intentar denuevo")
        validar_numero=True
while validar_hora:
    hora=int(input("hora del dia:"))
    if 0<=hora<=23:
        validar_hora=False
    else:
        print("hora invalida, intentar denuevo")
        validar_hora=True
numero=str(numero)
if 0<=hora<=7:
    print("CONTESTAR")
elif 7<hora<=14:
    if numero[5:8]=='909':
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 14<hora<17:
    print("NO CONTESTAR")
elif 17<=hora<=19:
    if numero[0:3]=='877':
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
    
else:
    print("NO CONTESTAR")