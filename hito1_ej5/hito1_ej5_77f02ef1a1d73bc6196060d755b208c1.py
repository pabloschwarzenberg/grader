rut = input("Ingrese rut sin dígito verificador: ")
rutl = list(rut)
factores = [2, 3, 4, 5, 6, 7, 2, 3]
suma = sum(int(digito) * factor for digito, factor in zip(rutl[::-1], factores))
dv = 11 - (suma % 11)

if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

print("dv=",dv)
