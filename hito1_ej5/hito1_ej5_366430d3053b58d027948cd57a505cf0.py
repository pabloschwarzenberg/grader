# Digito verificador
# Entrada
rut = int(input("Ingrese rut: "))
# Proceso
pos1 = ((rut // 1) % 10) * 2
pos2 = ((rut // 10) % 10) * 3
pos3 = ((rut // 100) % 10) * 4
pos4 = ((rut // 1000) % 10) * 5
pos5 = ((rut // 10000) % 10) * 6
pos6 = ((rut // 100000) % 10) * 7
pos7 = ((rut // 1000000) % 10) * 2
pos8 = (rut // 10000000) * 3

# Suma
suma = pos1 + pos2 + pos3 + pos4 + \
       pos5 + pos6 + pos7 + pos8

# Modulo 11
modulo = suma // 11
# Resto de la division del modulo
resto = suma - (modulo * 11)
# Digito verificador
dv = 11 - resto

# Salida
# Eleccion del digitio verificador si es letra o numero
if dv == 11:
       dv = 0
       print("dv", "=", dv)
elif dv == 10:
       dv = "K"
       print("dv", "=", dv)
else:
       print("dv", "=", dv)

