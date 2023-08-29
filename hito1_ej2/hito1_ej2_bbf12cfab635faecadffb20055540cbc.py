mensaje1 = str(int(input("Ingrese el numero que está llamando: ")))
mensaje2 = int(input("Ingrese la hora a la que llama: "))
subcadena1 = mensaje1[5:8]
subcadena2 = mensaje1[0:3]
if 0 <= mensaje2 < 7:
        print("Contesta el telefono")
else:
    if mensaje2 < 14 and subcadena1 == "909":
        print("CONTESTAR")
    else:
        if mensaje2 <14:
            print("NO CONTESTAR")
        else:
            if 17<mensaje2<=19 and subcadena2 == "877":
                print("NO CONTESTAR")
            else:
                if 17< mensaje2 <19:
                    print("CONTESTAR")
                else:
                    if mensaje2 > 19:
                        print("NO CONTESTAR")