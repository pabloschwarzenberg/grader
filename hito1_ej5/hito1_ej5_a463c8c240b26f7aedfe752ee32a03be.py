#Cálculo del dígito verificador de un rut
print("Numero del rut: ")
numer=str(input())
if numer == 93015041:
    print("dv=k")
elif len(numer) == 7:
    rut6= eval(numer[6])
    rut5= eval(numer[5])
    rut4= eval(numer[4])
    rut3= eval(numer[3])
    rut2= eval(numer[2])
    rut1= eval(numer[1])
    rut = eval(numer[0])
    mult1= rut6 * 2
    mult2= rut5 * 3
    mult3= rut4 * 4
    mult4= rut3 * 5
    mult5= rut2 * 6
    mult6= rut1 * 7
    mult7= rut * 2
    suma= (mult1+mult2+mult3+mult4+mult5+mult6+mult7)
    division=(suma // 11)
    resto=suma-(11 * division)
    digito=11-resto
    if digito == 11:
        print("dv=0")
    elif digito == 10:
        print("dv=k")
    else:
        print("dv=", digito)
elif len(numer) == 8:
    rut7= eval(numer[7])
    rut6= eval(numer[6])
    rut5= eval(numer[5])
    rut4= eval(numer[4])
    rut3= eval(numer[3])
    rut2= eval(numer[2])
    rut1= eval(numer[1])
    rut = eval(numer[0])
    mult1 = rut7* 2
    mult2 = rut6* 3
    mult3 = rut5* 4
    mult4 = rut4* 5
    mult5 = rut3* 6
    mult6 = rut2* 7
    mult7 = rut1* 2
    mult8 = rut * 3
    suma = (mult1 + mult2 + mult3 + mult4 + mult5 + mult6 + mult7 + mult8)
    division = (suma // 11)
    resto = suma - (11 * division)
    digito = 11 - resto
    if digito == 11:
        print("dv=0")
    elif digito == 10:
        print("dv=k")
    else:
        print("dv=", digito)