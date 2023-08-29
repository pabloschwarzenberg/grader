#Descomponer un número
Numero = int(input("Ingrese Un numero de hasta 4 digitos"))
LargoNumero = str(Numero)


if (Numero <1 or Numero > 9999):
    print ("Deben ser hasta 4 digitos")
elif 1 <= Numero <= 9999:
    UltimoDigito = Numero%10
    Numero = Numero //10

    TercerDigito = Numero%10
    Numero = Numero//10

    SegundoDigito = Numero%10
    Numero == Numero//10

    PrimerDigito = Numero//10

    if len (LargoNumero) == 4:
        print (str(PrimerDigito)+"M+"+str(SegundoDigito)+"C+"+str(TercerDigito)+"D+"+str(UltimoDigito)+"U")

    if len (LargoNumero) == 3:
        print (str(SegundoDigito)+"C+"+str(TercerDigito)+"D+"+str(UltimoDigito)+"U")

    if len (LargoNumero) == 2:
        print (str(TercerDigito)+"D+"+str(UltimoDigito)+"U")

    if len (LargoNumero) == 1:
        print (str(UltimoDigito)+"U")