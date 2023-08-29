#Cálculo del dígito verificador de un rut
rut = input("Ingrese el rut: ")
x1 = rut[0:1]
x2 = rut[1:2]
x3 = rut[2:3]
x4 = rut[3:4]
x5 = rut[4:5]
x6 = rut[5:6]
x7 = rut[6:7]
x8 = rut[7:8]
if rut(0,8):
    mys = x8*2+x7*3+x6*4+x5*5+x4*6+x3*7+x2*2+x1*3
    div = mys/11
    diva = mys-(11*div)
    rest = 11-diva
    if rest ==11:
          print("digito verificador es 0")
          print(f"rut: {rut}-0")
    elif rest==10:
        print("digito verificador es K")
        print(f"rut: {rut}-K")
    else:
        print(f"digito verificador es {rest}")
        print(f"rut: {rut}-{rest}")
elif rut(0,7):
    mys1 = x7*2+x6*3+x5*4+x4*5+x3*6+x2*7+x1*2
    div1 = mys1/11
    diva1 = mys1-(11*div1)
    rest1 = 11-diva1
    if rest1 ==11:
        rest1 = 0
        print("digito verificador es 0")
        print(f"rut: {rut}-{rest1}")
    elif rest1==10:
        rest1 = "K"
        print("digito verificador es K")
        print(f"rut: {rut}-{rest1}")
    else:
        rest1 = rest1
        print(f"digito verificador es {rest1}")
        print(f"rut: {rut}-{rest1}")