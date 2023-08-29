#Contestador de celular
numero_de_telefono = int(input("ingresar numero de telefono: "))
hora = int(input("ingresar hora: "))
ultimos = int(str(numero_de_telefono)[-3:])
contestar = False
primeros = int(str(numero_de_telefono)[3:])

if hora >= 0 and hora <= 7:
    contestar = True
elif hora < 14 and  ultimos == 909:
    contestar = True
if hora > 17 and hora < 19 and primeros != 877:
    contesta = True
if contestar:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
