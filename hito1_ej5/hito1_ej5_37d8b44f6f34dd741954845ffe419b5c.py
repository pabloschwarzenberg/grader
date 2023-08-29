#Cálculo del dígito verificador de un rut

rut = int(input("Ingrese su rut para calcular el digito verificador ->"))

if len(str(rut)) == 7:
    a = str(rut)
    b = int(a[6])
    c = int(a[5])
    d = int(a[4])
    e = int(a[3])
    f = int(a[2])
    g = int(a[1])
    h = int(a[0])
    num1 = b * 2
    num2 = c * 3
    num3 = d * 4
    num4 = e * 5
    num5 = f * 6
    num6 = g * 7
    num7 = h * 2
    suma = num1 + num2 + num3 + num4 + num5 + num6 + num7
    modulo11 = int(suma / 11)
    operatoria = suma -(11 * modulo11)
    if operatoria == 11:
        print("dv = 0")
        
    if operatoria == 10:
        print("dv = K")
        
    if operatoria != 10 or operatoria != 11:
        print("dv =", operatoria )
    
if len(str(rut)) == 7:
    a = str(rut)
    b = int(a[7])
    c = int(a[6])
    d = int(a[5])
    e = int(a[4])
    f = int(a[3])
    g = int(a[2])
    h = int(a[1])
    i = int(a[0])
    num1 = b * 2
    num2 = c * 3
    num3 = d * 4
    num4 = e * 5
    num5 = f * 6
    num6 = g * 7
    num7 = h * 2
    num8 = i * 3
    suma = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8
    modulo11 = int(suma / 11)
    operatoria = suma -(11 * modulo11)
    if operatoria == 11:
        print("dv = 0")
        
    if operatoria == 10:
        print("dv = K")
        
    if operatoria != 10 or operatoria != 11:
        print("dv =", operatoria )