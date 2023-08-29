#Zodiaco
enero = 1
febrero = 2
marzo = 3
abril = 4
mayo = 5
junio = 6
julio = 7
agosto = 8
septiembre = 9
octubre = 10
noviembre = 11
diciembre = 12

print("dia de necimiento")
dia = eval(input())
print("mes de nacimiento")
mes = eval(input())

while(dia > 31) or (mes > 12) or (dia < 1) or (mes < 1):
    print("introduzca otro dia")
    dia = eval(input())
    print("introduzca otro mes")
    mes = eval(input())
if(dia >= 21) and (mes == 3) or (dia <= 19) and (mes == 4):
    print("usted es aries")
else:
    if(dia >= 20) and (mes == 4) or (dia <= 20) and (mes == 5):
        print("usted es tauro")
    else:
        if(dia >= 21) and (mes == 5) or (dia <= 20) and (mes == 6):
            print("usted es geminis")
        else:
            if(dia >= 21) and (mes == 6) or (dia <= 22) and (mes == 7):
                print("usted es cáncer")
            else:
                if(dia >= 23) and (mes == 7) or (dia <= 22) and (mes == 8):
                    print("usted es leo")
                else:
                    if(dia >= 23) and (mes == 8) or (dia <= 22) and (mes == 9):
                        print("usted es virgo")
                    else:
                        if(dia >= 23) and (mes == 9) or (dia <= 22) and (mes == 10):
                            print("usted es libra")
                        else:
                            if(dia >= 23) and (mes == 10) or (dia <= 21) and (mes == 11):
                                print("usted es escorpio")
                            else:
                                if(dia >= 16) and (mes == 12) or (dia <= 16) and (mes == 1):
                                    print("usted es sagitario")
                                else:
                                    if(dia >= 19) and (mes == 1) or (dia <= 15) and (mes == 2):
                                        print("usted es capricornio")
                                    else:
                                        if(dia >= 16) and (mes == 2) or (dia <= 11) and (mes == 3):
                                            print("usted es acuario")
                                        else:
                                            if(dia >= 12) and (mes == 3) or (dia <= 18) and (mes == 4):
                                                print("usted es pisis")