#Cálculo del dígito verificador de un rut
rut = int(input("mencione su rut sin digito verificador, sin puntos ni guion: "))
if 999999 < rut < 10000000:
    print()
    a = rut // 1000000
    b = (rut // 100000) % 10
    c = (rut // 10000) % 10
    d = (rut // 1000) % 10
    e = (rut // 100) % 10
    f = (rut // 10) % 10
    g = (rut // 1) % 10

    print("el rut sin digito quedaria manera: ",a,b,".",c,d,e,".",f,g, )
    print()
    print("hallaremos el digito verificador")
    digito1 = 2 * g
    digito2 = 3 * f
    digito3 = 4 * e
    digito4 = 5 * d
    digito5 = 6 * c
    digito6 = 7 * b
    digito7 = 2 * a
    
    S = (digito1 + digito2 + digito3 + digito4 + digito5 + digito6 + digito7 )
    resto = S % 11
    dv = 11 - resto
    if dv == 11:
        print("dv=", 0,)
    elif dv == 10:
        print("dv=k")
    elif dv != 10 or dv != 11:
        print("dv=",dv,)
elif 9999999 < rut < 100000000:
    print()
    a = rut // 10000000
    b = (rut // 1000000) % 10
    c = (rut // 100000) % 10
    d = (rut // 10000) % 10
    e = (rut // 1000) % 10
    f = (rut // 100) % 10
    g = (rut // 10) % 10
    h = (rut // 1) % 10

    print("el rut sin digito quedaria manera: ",a,b,".",c,d,e,".",f,g, )
    print()
    print("hallaremos el digito verificador")
    digito1 = 2 * h
    digito2 = 3 * g
    digito3 = 4 * f
    digito4 = 5 * e
    digito5 = 6 * d
    digito6 = 7 * c
    digito7 = 2 * b
    digito8 = 3 * a
    
    S = (digito1 + digito2 + digito3 + digito4 + digito5 + digito6 + digito7 + digito8 )
    resto = S % 11
    dv = 11 - resto
    if dv == 11:
        print("dv=", 0,)
    elif dv == 10:
        print("dv=k")
    elif dv != 10 or dv != 11:
        print("dv=",dv,)
else:
    print("te falta cifras o te excediste")