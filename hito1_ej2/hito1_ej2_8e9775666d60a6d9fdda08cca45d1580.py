#Contestador de celular
num = int(input("Ingrese numero telefonico: "))
time = int(input("Ingrese hora de la llamada: "))

X1 = num%1000
X2 = num%-1000

if (time>=0) and (time<=7) and (num>=10000000) and (num<=99999999):
    if (num>=10000000) and (num<=99999999):
        print("Resultado: CONTESTAR")

    else:
        if (num<10000000) or (num>99999999):
            print("Resultado: NO CONTESTAR")
            
        elif (num<10000000) or (num>99999999):
            print("Resultado: NO CONTESTAR")

if (time>=8) and (time<=13) and (num>=10000000) and (num<=99999999) and (X1 != 909):
    if (num>=10000000) and (num<=99999999):
        print("Resultado: NO CONTESTAR")
    if (num>=10000000) and (num<=99999999):
        print("Resultado: CONTESTAR")

    else:
        if (num<10000000) or (num>99999999):
            print("Resultado: NO CONTESTAR")


elif (time>=8) and (time<=13) and (num>=10000000) and (num<=99999999) and (X1 == 909):
    print("Resultado: CONTESTAR")

if (time>=14) and (time<=16) and (num>=10000000) and (num<=99999999):
    print("Resultado: CONTESTAR")
    if (num<10000000) or (num>99999999):
        print("Resultado: NO CONTESTAR")


if (time>=17) and (time<=19) and (num>=10000000) and (num<=99999999) and (X2 == 877):
    print("Resultado: CONTESTAR")
    if (num<10000000) or (num>99999999):
        print("Resultado: NO CONTESTAR")

        
elif (time>=17) and (time<=19) and (num>=10000000) and (num<=99999999) and (X2 != 877):
    print("Resultado: NO CONTESTAR")
    if (num<10000000) or (num>99999999):
        print("Resultado: NO CONTESTAR")

if (time>19) and (time<=23) and (num>=10000000) and (num<=99999999):
    print("Resultado: NO CONTESTAR")
    if (num<10000000) or (num>99999999):
        print("Resultado: NO CONTESTAR")