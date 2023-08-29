numero=input("ingrese numero: ")
numero=int(numero)
hora=input("hora: ")
hora=int(hora)
if 7>hora>00:
    print("CONTESTAR")
if 14>hora>7:
    if numero%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if 19>hora>17:
    if numero//100000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if hora>19:
    print("NO CONTESTAR")