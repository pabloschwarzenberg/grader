#Cálculo del dígito verificador de un rut
Rut = input("Ingrese su rut: ")
Rut2 = int(Rut)
if Rut2 >= 10000000:
 Opc1 = int(Rut[7])
 Uno = Opc1*2
 Opc2 = int(Rut[6])
 Dos = Opc2*3
 Opc3 = int(Rut[5])
 Tres = Opc3*4
 Opc4 = int(Rut[4])
 Cuatro = Opc4*5
 Opc5 = int(Rut[3])
 Cinco = Opc5*6
 Opc6 = int(Rut[2])
 Seis = Opc6*7
 Opc7 = int(Rut[1])
 Siete = Opc7*2
 Opc8 = int(Rut[0])
 Ocho = Opc8*3
 
else: 
    Uno = 0
    Opc2 = int(Rut[6])
    Dos = Opc2*2
    Opc3 = int(Rut[5])
    Tres = Opc3*3
    Opc4 = int(Rut[4])
    Cuatro = Opc4*4
    Opc5 = int(Rut[3])
    Cinco = Opc5*5
    Opc6 = int(Rut[2])
    Seis = Opc6*6
    Opc7 = int(Rut[1])
    Siete = Opc7*7
    Opc8 = int(Rut[0])
    Ocho = Opc8*2
Suma = (Uno + Dos + Tres + Cuatro + Cinco + Seis + Siete + Ocho)
Division = (Suma/11)
Division1 = "%.1i"%Division
Division2 = int(Division1)
Calculo = Division2*11
Calculo1 =  Suma - (Calculo)
Final = 11 - Calculo1
if Final == 11:
    print("dv=0")
elif Final == 10:
    print("dv=k")
else:
    print("dv=",Final)