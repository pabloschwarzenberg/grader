nun = str(input("ingrese Numero telefonico de 8 digitos: "))
nun3 = (str(nun)[:3])
nun2 = (str(nun)[-3:])
hora = str(input("ingrese la hora de la llamada: "))
if hora>="00" and hora<="07":
    print("CONTESTAR")
if hora>="07" and hora<"14":
    if nun2 == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if hora>="17" and hora<"19":
    if nun3 == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if hora>="19" and hora<="23":
    print("NO CONTESTAR")