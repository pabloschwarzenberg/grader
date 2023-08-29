rut = input("ingrese su rut: ")
if (len(rut) == 8):
    n1 = int(input(rut[7]) * 2)
    n2 = int(input(rut[6]) * 3)
    n3 = int(input(rut[5]) * 4)
    n4 = int(input(rut[4]) * 5)
    n5 = int(input(rut[3]) * 6)
    n6 = int(input(rut[2]) * 7)
    n7 = int(input(rut[1]) * 2)
    n8 = int(input(rut[0]) * 3)
    total= n1+n2+n3+n4+n5+n6+n7+n8

if (len(rut) == 7):
    n1 = int(input(rut[6]) * 2)
    n2 = int(input(rut[5]) * 3)
    n3 = int(input(rut[4]) * 4)
    n4 = int(input(rut[3]) * 5)
    n5 = int(input(rut[2]) * 6)
    n6 = int(input(rut[1]) * 7)
    n7 = int(input(rut[0]) * 2)
    total=n1+n2+n3+n4+n5+n6+n7
verificador = int(total/11)
calulo = total-(11*verificador)
resta = 11-calculo
if (resta == 10):
    resta == "k"
    print("dv=",resta)
elif(resta == 11):
    resta = "0"
    print("dv=",resta)
else:
    print("dv=",resta)