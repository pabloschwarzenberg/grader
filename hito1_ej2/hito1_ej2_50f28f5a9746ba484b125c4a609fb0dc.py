from os import system
system ("cls")

while True:
    telf=list(input("Ingrese numero telefonico (8 cifras): "))
    hora=int(input("Ingrese hora (0 a 23): "))
    if len(telf)==8:
        if hora>=0 and hora<=23:
            break
        else:
            print("Ingrese hora valida")
    else:
        print("Ingrese numero telefonico valido")


if hora>=0 and hora<=7:
    print("CONTESTAR")

elif hora>=8 and hora<=14:
    if telf[5]=="9" and telf[6]=="0" and telf[7]=="9":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

elif hora>=17 and hora<=19:
    if telf[0]=="8" and telf[1]=="7" and telf[2]=="7":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

else:
    print("NO CONTESTAR")