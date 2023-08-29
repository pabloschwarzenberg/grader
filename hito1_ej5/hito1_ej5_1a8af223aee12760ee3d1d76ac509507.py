#Cálculo del dígito verificador de un rut
r = eval(input("Ingrese su rut sin puntos ni digito verificador: "))
while (10000000 < r < 100000000):
    digitos = str(r)
    d1 = int(digitos[0])
    d2 = int(digitos[1])
    d3 = int(digitos[2])
    d4 = int(digitos[3])
    d5 = int(digitos[4])
    d6 = int(digitos[5])
    d7 = int(digitos[6])
    d8 = int(digitos[7])
    d_1 = d1 * 3
    d_2 = d2 * 2
    d_3 = d3 * 7
    d_4 = d4 * 6
    d_5 = d5 * 5
    d_6 = d6 * 4
    d_7 = d7 * 3
    d_8 = d8 * 2
    dt= d_1 + d_2 + d_3 + d_4 + d_5 + d_6 + d_7 + d_8
    pe = dt/11
    p_e = int(pe)
    pt = 11*p_e
    resto = dt-pt
    dv = 11 - resto
    print("dv=", dv)
    if (dv == 11):
        print("dv = 0")
    elif (dv == 10):
        print("dv= K")
    break
while (1000000 < r < 10000000):
    digitos = str(r)
    d1 = int(digitos[0])
    d2 = int(digitos[1])
    d3 = int(digitos[2])
    d4 = int(digitos[3])
    d5 = int(digitos[4])
    d6 = int(digitos[5])
    d7 = int(digitos[6])
    d_1 = d1 * 2
    d_2 = d2 * 7
    d_3 = d3 * 6
    d_4 = d4 * 5
    d_5 = d5 * 4
    d_6 = d6 * 3
    d_7 = d7 * 2
    dt= d_1 + d_2 + d_3 + d_4 + d_5 + d_6 + d_7
    pe = dt/11
    p_e = int(pe)
    pt = 11*p_e
    resto= dt-pt
    dv = 11-resto
    print("dv=",dv)
    if (dv == 11):
        print("dv=0")
    elif (dv == 10):
        print("dv=K")
    break     