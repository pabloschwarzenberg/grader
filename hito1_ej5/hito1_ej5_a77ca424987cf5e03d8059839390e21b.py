#Cálculo del dígito verificador de un rut
rut = int(input("rut: "))
while rut>=10000000:
    aa= (rut%10**1)*2
    a = (rut%10**2//10**1)*3
    b = (rut%10**3//10**2)*4
    c = (rut%10**4//10**3)*5
    d = (rut%10**5//10**4)*6
    f = (rut%10**6//10**5)*7
    g = (rut%10**7//10**6)*2
    h = (rut//10**7)*3
    suma = aa+a+b+c+d+f+g+h
    modulo = suma%11
    resta = 11-modulo
    if resta ==11:
        digito= 0
        print("dv=", digito)
    elif resta== 10:
        digito= "K"
        print("dv=", digito)
    else:
        print("dv=", resta)
    break
while rut <10000000:
    aa= (rut%10**1)*2
    a = (rut%10**2//10**1)*3
    b = (rut%10**3//10**2)*4
    c = (rut%10**4//10**3)*5
    d = (rut%10**5//10**4)*6
    f = (rut%10**6//10**5)*7
    h = (rut//10**6)*2
    suma = aa+a+b+c+d+f+h
    modulo = suma%11
    resta = 11-modulo
    if resta ==11:
        digito= 0
        print("dv=", digito)
    elif resta== 10:
        digito= "K"
        print("dv=", digito)
    else:
        print("dv=", resta)
    break      