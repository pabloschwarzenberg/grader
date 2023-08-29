##print("DV=", var)
rut=input("Ingrese el RUT sin puntos: ")
largo=len(rut)
acum=0
i=0
digito=""
if(largo==7):
    acum = acum + (int(rut[0]) * 2)
    acum = acum + (int(rut[1]) * 7)
    acum = acum + (int(rut[2]) * 6)
    acum = acum + (int(rut[3]) * 5)
    acum = acum + (int(rut[4]) * 4)
    acum = acum + (int(rut[5]) * 3)
    acum = acum + (int(rut[6]) * 2)
else:
    acum = acum + (int(rut[0]) * 3)
    acum = acum + (int(rut[1]) * 2)
    acum = acum + (int(rut[2]) * 7)
    acum = acum + (int(rut[3]) * 6)
    acum = acum + (int(rut[4]) * 5)
    acum = acum + (int(rut[5]) * 4)
    acum = acum + (int(rut[6]) * 3)
    acum = acum + (int(rut[7]) * 2)
acum=11-(acum%11)
digito=acum
if(acum==11):
    digito="0"
    print("dv=", digito)
elif(acum==10):
    digito="K"
    print("dv=", digito)
else:
    print("dv=", digito)
      