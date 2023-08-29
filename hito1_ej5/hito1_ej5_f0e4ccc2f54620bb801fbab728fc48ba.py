#Cálculo del dígito verificador de un rut
RUN = int(input())
Dígitos = str(RUN)
Lenght = len(Dígitos)
if 8 == Lenght:
    i = Dígitos[0:1:1]
    I = int(i)
    ii = Dígitos[1:2:1]
    II = int(ii)
    iii = Dígitos[2:3:1]
    III = int(iii)
    iv = Dígitos[3:4:1]
    IV = int(iv)
    v = Dígitos[4:5:1]
    V = int(v)
    vi = Dígitos[5:6:1]
    VI = int(vi)
    vii = Dígitos[6:7:1]
    VII = int(vii)
    viii = Dígitos[7:8:1]
    VIII = int(viii)
    M = (3*I+2*II+7*III+6*IV+5*V+4*VI+3*VII+2*VIII)
    R = (M % 11)
    D = 11 - R
    if D == 10:
        print("dv=K")
    elif R == 0:
        print("dv={}".format(R))
    else:
        print("dv={}".format(D))
else:
    i = Dígitos[0:1:1]
    I = int(i)
    ii = Dígitos[1:2:1]
    II = int(ii)
    iii = Dígitos[2:3:1]
    III = int(iii)
    iv = Dígitos[3:4:1]
    IV = int(iv)
    v = Dígitos[4:5:1]
    V = int(v)
    vi = Dígitos[5:6:1]
    VI = int(vi)
    vii = Dígitos[6:7:1]
    VII = int(vii)
    m = 2*I+7*II+6*III+5*IV+4*V+3*VI+2*VII
    r = m % 11
    d = 11 - r
    if d == 10:
        print("dv=K")
    elif r == 0:
        print("dv={}".format(r))
    else:
        print("dv={}".format(d))