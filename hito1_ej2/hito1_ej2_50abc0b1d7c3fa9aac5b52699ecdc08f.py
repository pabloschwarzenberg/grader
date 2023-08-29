#Contestador de celular
cel = int(input("Desde que numero está llamando?: "))
hora = int(input("Que hora es?: "))
final = cel % 1000
inicio= cel // 10000
if (hora >= 0) and (hora <= 7):
    print("CONTESTAR")
else:
    if hora <14 and hora>7:
        if final == 909:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    else:
        if hora <14 and hora>7:
            print("NO CONTESTAR")
        else:
             if hora >= 17 and hora <= 19:
                 if inicio == 877:
                    print("CONTESTAR")
                 else:
                     print("NO CONTESTAR")
             else:
                 print("NO CONTESTAR")