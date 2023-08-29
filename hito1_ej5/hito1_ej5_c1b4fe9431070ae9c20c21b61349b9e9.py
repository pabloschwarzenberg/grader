#Cálculo del dígito verificador de un rut
def digito(a):
    if len(a) ==7:
        n1 = int(a[6]) * 2
        n2 = int(a[5]) * 3
        n3 = int(a[4]) * 4
        n4 = int(a[3]) * 5
        n5 = int(a[2]) * 6
        n6 = int(a[1]) * 7
        n7 = int(a[0]) * 2
        suma = n1 + n2 + n3 + n4 + n5 + n6 + n7
        division = int(suma/11)
        validacion = 11-(suma - (11*division))
        if validacion == 11:
            print("dv=0")
        elif validacion == 10:
            print("dv=k")
        else:
            print("dv={}".format(validacion))
    elif len(a) ==8:
        n1 = int(a[7]) * 2
        n2 = int(a[6]) * 3
        n3 = int(a[5]) * 4
        n4 = int(a[4]) * 5
        n5 = int(a[3]) * 6
        n6 = int(a[2]) * 7
        n7 = int(a[1]) * 2
        n8 = int(a[0]) * 3
        suma = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
        division = int(suma / 11)
        validacion = 11-(suma - (11*division))
        if validacion == 11:
            print("dv=0")
        elif validacion == 10:
            print("dv=k")
        else:
            print("dv={}".format(validacion))

a = input("ingrese rut ")
digito(a)     