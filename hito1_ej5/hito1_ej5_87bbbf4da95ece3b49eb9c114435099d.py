a = int(input("Ingrese numero de rut(sin digito verificador:)"))
while len(str(a)) < 7 or len(str(a)) > 8:
    a = int(input("Ingrese numero de rut(sin digito verificador:)"))

if len(str(a)) == 8:
    sa = str(a)
    b = sa[7]
    c = sa[6]
    d = sa[5]
    e = sa[4]
    f = sa[3]
    g = sa[2]
    h = sa[1]
    i = sa[0]
    z1 = int(b)*2
    z2 = int(c)*3
    z3 = int(d)*4
    z4 = int(e)*5
    z5 = int(f)*6
    z6 = int(g)*7
    z7 = int(h)*2
    z8 = int(i)*3
    z = z1+z2+z3+z4+z5+z6+z7+z8
    x = int(z/11)
    y = z - (int(x)*11)
    w = 11-y
    if w == 11:
        print("dv = ",0)
    elif w == 10:
        print("dv = K")
    else:
        print("dv = ",w)

elif len(str(a)) == 7:
    sa = str(a)
    c = sa[6]
    d = sa[5]
    e = sa[4]
    f = sa[3]
    g = sa[2]
    h = sa[1]
    i = sa[0]
    z2 = int(c)*2
    z3 = int(d)*3
    z4 = int(e)*4
    z5 = int(f)*5
    z6 = int(g)*6
    z7 = int(h)*7
    z8 = int(i)*2
    z = z2 + z3 + z4 + z5 + z6 + z7 + z8
    x = int(z / 11)
    y = z - (int(x) * 11)
    w = 11 - y
    if w == 11:
        print("dv = ",0)
    elif w == 10:
        print("dv = K")
    else:
        print("dv =",w)