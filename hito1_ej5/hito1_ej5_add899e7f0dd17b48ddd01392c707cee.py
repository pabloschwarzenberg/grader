rut = int(input("Ingrese su RUT: "))
m = 2
suma = 0

while rut != 0:
    ultimo_digito = rut%10
    mp = ultimo_digito*m
    suma += mp
    rut = rut//10
    m += 1
    if m == 8:
        m = 2
print(suma)

resto = suma%11
dv = 11-resto
print("dv=",dv)