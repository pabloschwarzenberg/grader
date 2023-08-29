a=str(input("Numero del rut: "))
if a == 93015041:
    print("dv=k")
elif len(a) == 7:
    # i=eval(a[7])
    h = eval(a[6])
    
    g = eval(a[5])
    
    f = eval(a[4])
    
    e = eval(a[3])
    
    d = eval(a[2])
    
    c = eval(a[1])
    
    b = eval(a[0])
    
    
    
    b1 = h * 2
    
    c1 = g * 3
    
    d1 = f * 4
    
    e1 = e * 5
    
    f1 = d * 6
    
    g1 = c * 7
    
    h1 = b * 2
    
    suma_de_productos = (b1 + c1 + d1 + e1 + f1 + g1 + h1)
    division = (suma_de_productos // 11)
    resto = suma_de_productos - (11 * division)
    verificador = 11 - resto
    if verificador == 11:
        print("dv=0")
    elif verificador == 10:
        print("dv=k")
    else:
        print("dv=", verificador)
elif len(a) == 8:
    i = eval(a[7])
    
    h = eval(a[6])
    
    g = eval(a[5])
    
    f = eval(a[4])
    
    e = eval(a[3])
    
    d = eval(a[2])
    
    c = eval(a[1])
    
    b = eval(a[0])
    
    a1 = i * 2
    
    b1 = h * 3
    
    c1 = g * 4
    
    d1 = f * 5
    
    e1 = e * 6
    
    f1 = d * 7
    
    g1 = c * 2
    
    h1 = b * 3
    
    suma_de_productos = (a1 + b1 + c1 + d1 + e1 + f1 + g1 + h1)
    division = (suma_de_productos // 11)
    resto = suma_de_productos - (11 * division)
    verificador = 11 - resto
    if verificador == 11:
        print("dv=0")
    elif verificador == 10:
        print("dv=k")
    else:
        print("dv=", verificador)