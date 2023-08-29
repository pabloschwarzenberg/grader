rut = int(input("Ingrese RUT sin puntos ni dígito verificador: "))
x1 = rut%10
x2 = (rut%100) // 10
x3 = (rut%1000) // 100
x4 = (rut%10000) // 1000
x5 = (rut%100000) // 10000
x6 = (rut%1000000) // 100000
x7 = (rut%10000000) // 1000000
x8 = (rut%100000000) // 10000000
x1a = x1 * 2
x2a = x2 * 3
x3a = x3 * 4
x4a = x4 * 5
x5a = x5 * 6
x6a = x6 * 7
x7a = x7 * 2
x8a = x8 * 3
sumatoria = x1a + x2a + x3a + x4a + x5a + x6a + x7a + x8a
modulo = sumatoria % 11
digito = 11 - modulo
if(digito == 11):
    final = 0
    print("dv=",final)
else:
    if(digito == 10):
        final = "K"
        print("dv=",final)
    else:
        final = digito
        print("dv=",final)