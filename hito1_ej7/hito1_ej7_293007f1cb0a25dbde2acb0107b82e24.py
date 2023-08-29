# Signo del Zodíaco
# 2 points possible (ungraded)
# Escribe un programa que reciba como parámetro el día y el mes del cumpleaños de una persona (como números enteros) y 
# que imprima el signo del zodíaco al que pertenece.

# Para determinar las fechas de cada signo utiliza la columna Tropical Zodiac en la tabla de fechas que aparece en este link (Wikipedia).

#Zodiaco
dia = int(input("Ingrese su día de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento: "))

#Filtrar posibles signos

if mes == 1 and dia <= 20:
    print("Acuario")
else:
    if mes == 2 and dia <= 19:
        print("Acuario")
    else:
        if mes == 2 and dia >= 20:
            print("Piscis")
        else:
            if mes == 3 and dia <= 21:
                print("Piscis")
            else:
                if mes == 3 and dia >= 21:
                    print("Aries")
                else:
                    if mes == 4 and dia <= 20:
                        print("Aries")
                    else:
                        if mes == 4 and dia >= 20:
                            print("Tauro")
                        else:
                            if mes == 5 and dia <= 21:
                                print("Tauro")
                            else:
                                if mes == 5 and dia >= 21:
                                    print("Geminis")
                                else:
                                    if mes == 6 and dia <= 21:
                                        print("Geminis")
                                    else:
                                        if mes == 6 and dia >= 21:
                                            print("Cancer")
                                        else:
                                            if mes == 7 and dia <= 23:
                                                print("Cancer")
                                            else:
                                                if mes == 7 and dia >= 23:
                                                    print("Leo")
                                                else:
                                                    if mes == 8 and dia <= 23:
                                                        print("Leo")
                                                    else:
                                                        if mes == 8 and dia >= 23:
                                                            print("Virgo")
                                                        else:
                                                            if mes == 9 and dia <= 23:
                                                                print("Virgo")
                                                            else:
                                                                if mes == 9 and dia >= 23:
                                                                    print("Libra")
                                                                else:
                                                                    if mes == 10 and dia <= 23:
                                                                        print("Libra")
                                                                    else:
                                                                        if mes == 10 and dia <= 23:
                                                                            print("Scorpio")
                                                                        else:
                                                                            if mes == 11 and dia <= 22:
                                                                                print("Scorpio")
                                                                            else:
                                                                                if mes == 11 and dia >= 22:
                                                                                    print("Sagitario")