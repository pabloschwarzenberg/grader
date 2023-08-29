numero = input("Ingrese numero de 4 digitos : ")

if int(numero)>999:

    M= str(numero[0:1])
    C= str(numero[1:2])
    D= str(numero[2:3])
    U= str(numero[3:4])
    print ('%dM + %dC + %dD + %dU' %(int(M),int(C),int(D),int(U)))

elif int(numero)<100:

    D= str(numero[0:1])
    U= str(numero[1:2])

    print ('%dD + %dU' %(int(D),int(U)))

elif int(numero)>99:
    C= str(numero[0:1])
    D= str(numero[1:2])
    U= str(numero[2:3])

    print ('%dC + %dD + %dU' %(int(C),int(D),int(U)))
