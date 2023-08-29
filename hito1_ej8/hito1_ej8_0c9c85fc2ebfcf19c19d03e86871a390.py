#Descomponer un número

nro = input("Ingrese numero: ")

largo = len(nro)
#str(largo)


if largo==1:
    print(str(nro) +"U")

elif largo==2:
    print(str(nro[0]) +"D+" + str(nro[1]) +"U" )

elif largo==3:
    print(str(nro[0]) + "C+" + str(nro[1]) + "D+" +  str(nro[2]) +"U"  )

elif largo==4:
    print(str(nro[0]) +"M+" + str(nro[1]) +"C+" + str(nro[2]) + "D+" + str(nro[3]) + "U"  )