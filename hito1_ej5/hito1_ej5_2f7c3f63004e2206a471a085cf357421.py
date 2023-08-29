#Cálculo del dígito verificador de un rut

rut = int(input("Ingrese el rut para saber su digito verificador(ej: 12345678): "))

resto = rut
if len(str(rut))== 8:
    prim = resto%10
    resto = resto//10
    seg = resto%10
    resto = resto//10
    terc = resto%10
    resto = resto//10
    cuarto = resto%10
    resto = resto//10
    quinto = resto%10
    resto = resto//10
    sexto = resto%10
    resto = resto//10
    sep = resto%10
    resto = resto//10
    oct = resto%10



    multi1 = prim*2
    multi2 = seg*3
    multi3 = terc*4
    multi4 = cuarto*5
    multi5 = quinto*6
    multi6 = sexto*7
    multi7 = sep*2
    multi8 = oct*3

    suma_total = (multi1 + multi2 + multi3 + multi4 + multi5+ multi6 + multi7 + multi8)

    resto_modulo = suma_total%11
    dv = 11 - resto_modulo

    if dv == 11:
        dv = 0
        
    if dv == 10:
        dv = "k"
        

    print("dv=",dv)





if len(str(rut))== 7:
    prim = resto%10
    resto = resto//10
    seg = resto%10
    resto = resto//10
    terc = resto%10
    resto = resto//10
    cuarto = resto%10
    resto = resto//10
    quinto = resto%10
    resto = resto//10
    sexto = resto%10
    resto = resto//10
    sep = resto%10


    multi1 = prim*2
    multi2 = seg*3
    multi3 = terc*4
    multi4 = cuarto*5
    multi5 = quinto*6
    multi6 = sexto*7
    multi7 = sep*2

    suma_total = (multi1 + multi2 + multi3 + multi4 + multi5+ multi6 + multi7)

    resto_modulo = suma_total%11
    dv = 11 - resto_modulo

    if dv == 11:
        dv = 0
        
    if dv == 10:
        dv = "k"
        
    print("dv=",dv)







