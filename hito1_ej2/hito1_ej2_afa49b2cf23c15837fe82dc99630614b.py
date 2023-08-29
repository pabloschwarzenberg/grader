numero=int(input("ingrese numero :"))
if numero<=9999999 or numero>=100000000:
    print("numero erroneo") 
hora=int(input("ingrese hora :"))
if hora<=-1 or hora>=24:
    print("hora erroneo")

#:::::::::::::::::::::::::::::::::::::::::
if hora<=7:
    print("CONTESTAR ☻")
if hora <=14 and hora>=7:
    if numero%1000==909:
        print("CONTESTAR ☻")
if hora <=19 and hora>=17:
    if numero%1000==877:
        print("CONTESTAR ☻")
    else:
            print("NO CONTESTAR ☻")
if hora>19:
    print("no contestar")
