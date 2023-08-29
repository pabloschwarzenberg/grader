#Cálculo del dígito verificador de un rut
rut = input("rut: ")

if len(rut) == 8:
    rutNuevo = [eval(rut[7]), eval(rut[6]), eval(rut[5]), eval(rut[4]), eval(rut[3]), eval(rut[2]), eval(rut[1]),
                eval(rut[0])]
    lista = [2, 3, 4, 5, 6, 7, 2, 3]

else:
    rutNuevo = [eval(rut[6]), eval(rut[5]), eval(rut[4]), eval(rut[3]), eval(rut[2]), eval(rut[1]), eval(rut[0])]
    lista = [2, 3, 4, 5, 6, 7, 2]

producto = [a * b for a, b in zip(rutNuevo, lista)]

suma = sum(producto)

casiFinal = 11 - (suma % 11)

if casiFinal == 11:
    dv = "0"
elif casiFinal == 10:
    dv = "K"
else:
    dv = casiFinal

print("dv={}".format(dv))      