from time import sleep
NT=int(input("Ingrese numero telefonico:"))
H=int(input("Ingrese hora de llamada:"))

while True:
    if H>=0 and H<=7:
        print("CONTESTAR")
        sleep(1)
    if H<14:
        if NT%1000==909:
            print("CONTESTAR")
            sleep(1)
            break
    if H>=17 and H<=19:
        if NT/1000==877:
            print("CONTESTAR")
            sleep(1)
            break
    if H>19:
        print("NO CONTESTAR")
        break
    else:
        print("NO CONTESTAR")
        sleep(1)
        break
