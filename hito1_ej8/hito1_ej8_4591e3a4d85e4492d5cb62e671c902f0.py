#Descomponer un número
print("DESCOMPONER UN NUMERO")
NRO = int(input("INGRESE UN NUMERO DE MAXIMO 4 DIGITOS: "))
if NRO<0 or NRO>9999:
    print("ERROR")
    print("EL NUMERO INGRESADO NO ES VALIDO")
    print("INGRESE UN NUMERO DE 4 O MENOS DIGITOS POSITIVO")
else:
    N1 = int(NRO/1000)
    N2 = int((NRO-(N1*1000))/100)
    N3 = int((NRO-(N1*1000+N2*100))/10)
    N4 = int((NRO-(N1*1000+N2*100+N3*10)))
    print(N1,"M +",N2,"C +",N3,"D +",N4,"U")      