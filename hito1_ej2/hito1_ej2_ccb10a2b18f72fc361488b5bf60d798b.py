num = int(input("ingrese el numero de celular (8 digitos): "))
hora = int(input("ingrese la hora ( entre 0 y 23): "))
final = num % 1000
inicio = num // 100000
if hora >=0 and hora <=7:
    print("CONTESTAR")
else:
    if hora >7 and hora <=14:
        if final == 909:
            print("CONTESTAR")
        else:
                print("NO CONTESTAR")
    else:
                if hora >=17 and hora <=19:
                        if 877 == inicio:
                            print("NO CONTESTAR")
                        else:
                            print("CONTESTAR")
                else:
                                if hora >19 and hora <=23:
                                    print("NO CONTESTAR")
