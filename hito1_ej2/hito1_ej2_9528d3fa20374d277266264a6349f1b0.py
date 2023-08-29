#Contestador
n = int(input("Ingrese un numero telefonico: "))
h = int(input("Ingrese una hora entre 23 y 0 en la que desea llamar: "))
num = n // 1000
num2 = n // 1000
if n >= 10000000 and n <= 99999999:

  if h < 24 and h > -1:
    if h >= 0 and h <= 7:
        print("CONTESTAR")
    else:
        if h > 7 and h < 14 or num == 909:
            print("CONTESTAR")
        else:
            if h == 14:
                print("CONTESTAR")
            else:
                if h == 15 or h == 16:
                    print("CONTESTAR")
                else:
                    if num2 == 877 and h > 17 and h < 19:
                        print("CONTESTAR")
                    else:
                        if h > 17 and h < 19:
                            print("NO CONTESTAR")
                        else:
                         if h > 19 and h < 23:
                           print("NO CONTESTAR")
                         else: print("NO CONTESTAR")

  else: print("Ingrese un valor que esté en el rango de horas disponibles")
else: print("Ingrese un numero telefonico valido")

