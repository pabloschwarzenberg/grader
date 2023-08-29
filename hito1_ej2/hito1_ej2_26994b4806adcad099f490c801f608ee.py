#Contestador de celular
numero=int(input("Ingrese numero telefónico de 8 cifras:"))
hora=int(input("Ingrese hora de llamada (entre 0 y 23):"))
ultnum= numero%1000
primnum= numero//100000

if hora>=0 and hora<=7:
    print("CONTESTAR")
else:
    if hora>7 and hora<14 and ultnum == 909:
        print("CONTESTAR")
    else:
        if hora>7 and hora<14:
            print("NO CONTESTAR")
        else:
            if hora>17 and hora<19 and primnum == 877:
                print("NO CONTESTAR")
            else:
                if hora>17 and hora <19:
                    print("CONTESTAR")
                else:
                    print("NO CONTESTAR")
      