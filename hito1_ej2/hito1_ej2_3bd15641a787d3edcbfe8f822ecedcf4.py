a=int(input("ingrese numero telefonico: "))
b=int(input("ingrese hora de llamada: "))
numero_909=int(a%1000)
numero_887=int(a//100000)
if b>=0 and b <=7:
    print("CONTESTAR")
else:
    if numero_909==909:
        print("CONTESTAR")
    else:
        if  b>=8 and b<14:
            print("NO CONTESTAR")
        else:
            if numero_887==877:
                print("NO CONTESTAR")
            else:
                if b>=17 and b<=19:
                    print("NO CONTESTAR")
                else:
                    if b>=17 and b<19:
                      print("CONTESTAR")
                    else:
                        if b>19:
                            print("NO CONTESTAR")  