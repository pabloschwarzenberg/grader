# Cálculo del dígito verificador de un rut
r = str(input())
a = 2 * int(r[-1])
b = 3 * int(r[-2])
c = 4 * int(r[-3])
d = 5 * int(r[-4])
e = 6 * int(r[-5])
f = 7 * int(r[-6])
g = 2 * int(r[-7])
if len(r) == 8:
    h = 3 * int(r[-8])
    t = a + b + c + d + e + f + g + h
    m_t = t % 11
    d_v = 11 - m_t
    if d_v == 11:
        print("dv=0")
    elif d_v == 10:
        print("dv=K")
    else:
        print("dv={}".format(d_v))
else:
    t = a + b + c + d + e + f + g
    m_t = t % 11
    d_v = 11 - m_t
    if d_v == 11:
        print("dv=0")
    elif d_v == 10:
        print("dv=K")
    else:
        print("dv={}".format(d_v))
