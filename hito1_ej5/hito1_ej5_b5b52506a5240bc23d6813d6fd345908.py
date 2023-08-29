#Cálculo del dígito verificador de un rut
# Entradas
rut = input("Ingrese su rut: ")
dv = ""
# Procesamiento
if len(rut) == 8:
    a = rut[-1]
    a = int(a)
    b = rut[-2]
    b = int(b)
    c = rut[-3]
    c = int(c)
    d = rut[-4]
    d = int(d)
    e = rut[-5]
    e = int(e)
    f = rut[-6]
    f = int(f)
    g = rut[-7]
    g = int(g)
    h = rut[-8]
    h = int(h)
    a *= 2
    b *= 3
    c *= 4
    d *= 5
    e *= 6
    f *= 7
    g *= 2
    h *= 3
    total = a+b+c+d+e+f+g+h
    resto = total % 11
    dv = 11 - resto

elif len(rut) == 7:
    a = rut[-1]
    a = int(a)
    b = rut[-2]
    b = int(b)
    c = rut[-3]
    c = int(c)
    d = rut[-4]
    d = int(d)
    e = rut[-5]
    e = int(e)
    f = rut[-6]
    f = int(f)
    g = rut[-7]
    g = int(g)
    a *= 2
    b *= 3
    c *= 4
    d *= 5
    e *= 6
    f *= 7
    g *= 2
    total = a+b+c+d+e+f+g
    resto = total % 11
    dv = 11 - resto    

if dv == 11:
    digito_verificador = 0
elif dv == 10:
    digito_verificador = "K"
else:
    digito_verificador = dv
print("dv=",digito_verificador)
