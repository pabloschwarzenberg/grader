#Contestador de celular
numero= eval(input("ingrese numero telefonico"))
hora=eval(input("ingrese hora:"))

if (hora>=0) and (hora<=7):
    print("resultado:CONTESTAR")
elif (hora<=14):
    digitos=numero%1000
    if digitos==909:
        print("resultado:CONTESTAR")
    else:
        print("resultado:NO CONTESTAR")
elif (hora>=17) and (hora<=19):
    digitos=numero//100000
    if (digitos==877):
        print("resultado:NO CONTESTAR")
    else:
        print("resultado:CONTESTAR")
elif (hora>19):
    print("resultado:NO CONTESTAR")
else:
    print("resultado:NO CONTESTAR")
    

