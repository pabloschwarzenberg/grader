#Contestador de celular
numero=int(input("Ingrese su numero telefonico:"))
horario=int(input("ingrese la hora a la cual esta llamando:"))


while True:
    if numero>=0 and horario<=7:
        print("CONTESTAR")
    if horario<14:
        if numero%1000==909:
            print("CONTESTAR")
            break
    if horario>=17 and horario<=19:
        if numero//1000==877:
            print("CONTESTAR")
            break
    if horario>19:
        print("NO CONTESTAR")
        break
    else:
        print("NO CONTESTAR")
        break
