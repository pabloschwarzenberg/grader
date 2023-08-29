numero= float (input("Ingrese numero hasta 4 digitos: "))
while not numero>=0 and numero<=9999:
    numero= float (input("Error... Ingrese numero hasta 4 digitos: "))
UM=numero//1000
CEN= ((numero-(UM*1000))//100)
DECE= ((numero-(UM*1000)-(CEN*100))//10)
UNI= (numero - (UM*1000)-(CEN*100)-(DECE*10))

if UM==0:
    if CEN==0:
        if DECE==0:
            print(round(UNI),"U")
        else:
            print(round(DECE),"D+",round(UNI),"U")
    else:
        print(round(CEN),"C+",round(DECE),"D+",round(UNI),"U")
else:
    print(round(UM),"M+",round(CEN),"C+",round(DECE),"D+",round(UNI),"U")


