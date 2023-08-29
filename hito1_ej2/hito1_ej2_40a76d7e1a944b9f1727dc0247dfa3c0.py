telefono=int(input("escriba su numero de telefono de 8 cifras: "))
hora=int(input("escriba una hora: "))
final=int(str(telefono)[5:8])
inicial=int(str(telefono)[0:3])


if( hora>=0 and hora<=7 ):
    print("CONTESTAR")
elif( hora<14 and final==909 ):
    print("CONTESTAR")
elif( hora>=17 and hora<=19 and not inicial==877 ):
    print("CONTESTAR")
elif( hora>19 ):
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")