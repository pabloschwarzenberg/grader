#Cálculo del dígito verificador de un rut
RUT1 = eval(input("primer numero de su rut: "))
RUT2 = eval(input("segundo numero de su rut: "))
RUT3 = eval(input("tercer numero de su rut: "))
RUT4 = eval(input("cuarto numero de su rut: "))
RUT5 = eval(input("quinto numero de su rut: "))
RUT6 = eval(input("sexto numero de su rut: "))
RUT7 = eval(input("septimo numero de su rut: "))
RUT8 = eval(input("octavo numero de su rut: "))
K = "K"
Frut1 = RUT1 * 2
Frut2 = RUT2 * 3
Frut3 = RUT3 * 4
Frut4 = RUT4 * 5
Frut5 = RUT5 * 6
Frut6 = RUT6 * 7
Frut7 = RUT7 * 2
Frut8 = RUT8 * 3
TRUT = Frut1 + Frut2 + Frut3 + Frut4 + Frut5 + Frut6 + Frut7 + Frut8
Mrut = ( TRUT / 11)
Erut = TRUT - (11 * Mrut)
CodigoV = 11 - Erut
if CodigoV == 11:
    CodigoV = 0
if CodigoV == 10:
    CodigoV = K
print("dv= ",CodigoV)
print(K)