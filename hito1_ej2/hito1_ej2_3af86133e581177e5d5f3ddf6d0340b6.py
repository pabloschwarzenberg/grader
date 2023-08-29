#Contestador de celular
cel=int(input("Ingrese numero de celular: "))
hora=int(input("Ingrese hora de llamada: "))
regla0 = str(cel).endswith("909")
print(regla0)
regla1 = str(cel).startswith("877")
if(cel<9999999 or cel>99999999 ):
    print("NO CONTESTAR")
elif (hora<0 or hora>23):
    print("NO CONTESTAR")
elif (hora>=0 and hora<=7):
    print("CONTESTAR")
elif(hora<14):
    if(regla0):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif (hora>=17 and hora<=19 ) :
    if(regla1):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif (hora > 19 ):
        print("NO CONTESTAR")                 