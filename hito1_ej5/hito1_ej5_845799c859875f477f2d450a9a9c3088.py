num = int(input("Ingresa rut: "))

ln = str(num)
largo = len(ln)

if largo == 7:
    a = num % 10
    num = num //10
    b = num % 10
    num = num //10
    c = num % 10
    num = num //10
    d = num % 10
    num = num //10
    e = num % 10
    num = num //10
    f = num % 10
    g = num //10

    a = a * 2
    b = b * 3
    c = c * 4
    d = d * 5
    e = e * 6
    f = f * 7
    g = g * 2

    suma = a+b+c+d+e+f+g
    resto = suma % 11
    dv = 11 - resto
    if dv == 11:
        print("dv=0")
    elif dv == 10:
        print("dv=K")
    else:
        print("dv=",dv)
  
elif largo == 8:
    a = num % 10
    num = num //10
    b = num % 10
    num = num //10
    c = num % 10
    num = num //10
    d = num % 10
    num = num //10
    e = num % 10
    num = num //10
    f = num % 10
    num = num //10
    g = num % 10
    h = num //10

    a = a * 2
    b = b * 3
    c = c * 4
    d = d * 5
    e = e * 6
    f = f * 7
    g = g * 2
    h = h * 3
    
    suma = a+b+c+d+e+f+g+h
    resto = suma % 11
    dv = 11 - resto
    if dv == 11:
        print("dv=0")
    elif dv == 10:
        print("dv=K")
    else:
        print("dv=",dv)
  