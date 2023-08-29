print("ingrese la hora")
hora = int(input())
print("ingrese el numero")
numero = int(input())

v1 = numero % 1000

if(hora > 19):
    print("NO CONTESTAR")
else:
    if(hora >= 0) and (hora <= 7):
        print("CONTESTAR")
    else:
        if(hora < 14):
            print("NO CONTESTAR")
        else:
            if((hora >= 17 and hora <= 19 and not(numero // 100000))):
                print("CONTESTAR")
            else:
                print("NO CONTESTAR")