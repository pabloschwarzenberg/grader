numero = str(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese numero hora: "))

if hora >0 and hora <= 7:
    print ( "contestar")
elif numero [5:7] != 909 and hora >7 and hora <14:
    print ( "contestar")
elif numero [0:2] != 877 and hora >=17 and hora <19:
    print ( "no contestar")
elif hora >19 :
    print ( "no contestar")
else: print("contestar")
