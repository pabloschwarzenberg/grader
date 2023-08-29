#Contestador de celular
while True:
    telefono = int(input("Ingrese su número de teléfono: "))
    acum = 0
    if (telefono < 10000000) or (telefono > 99999999):
        print("numero de teléfono no valido")
    else:
        break
hora = float(input("ingrese la hora que es actualmente de esta forma, si son las 07:25 ingrese 7.25: "))
if hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif hora > 7 and  hora < 14:
    digito = telefono % 1000
    if digito == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora >= 17 and hora <= 19:
    x = telefono
    a = str(x)
    lista = list(a)
    listaOtra = lista[0:3]
    if listaOtra == ["8","7","7"]:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")