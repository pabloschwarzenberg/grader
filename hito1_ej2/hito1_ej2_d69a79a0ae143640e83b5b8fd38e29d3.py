numero_telefono=int(input("Numero de telefono:"))
hora=int(input("Hora de llamdada:"))
digitos=int(numero_telefono % 1000)
digitus=int(numero_telefono/100000)

if hora <7 and hora > 0:
    print("CONTESTAR")
elif hora<14 and hora>7 and digitos ==909 :
    print("CONTESTAR")
elif hora<19 and hora>17 and digitus !=877:
    print("CONTESTAR")
elif digitus ==877 :
    print("NO CONTESTAR")
elif hora>19 and hora<23 :
    print("NO CONTESTAR")   