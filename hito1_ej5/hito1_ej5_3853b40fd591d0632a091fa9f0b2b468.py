rut = int(input("Ingrese RUT sin puntos ni dígito verificador: "))
d1 = rut%10
d2 = (rut%100) // 10
d3 = (rut%1000) // 100
d4 = (rut%10000) // 1000
d5 = (rut%100000) // 10000
d6 = (rut%1000000) // 100000
d7 = (rut%10000000) // 1000000
d8 = (rut%100000000) // 10000000
d1a = d1 * 2
d2a = d2 * 3
d3a = d3 * 4
d4a = d4 * 5
d5a = d5 * 6
d6a = d6 * 7
d7a = d7 * 2
d8a = d8 * 3
sumatoria = d1a + d2a + d3a + d4a + d5a + d6a + d7a + d8a
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