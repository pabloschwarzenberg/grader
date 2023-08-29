#Contestador de celular
numero = int(input('Ingrese número de telefono: '))
s_numero = str(numero)
hora = int(input('Ingrese hora de llamada: '))
i_numero = s_numero[0:2]
f_numero = s_numero[5:7]

if hora >= 0 and hora <= 7:
    print("CONTESTAR LLAMADA")
elif hora<14:
    print("CONTESTAR LLAMADA")
elif hora >= 13 and hora < 14:
    print("CONTESTAR LLAMADA")
elif hora >= 8 and hora <= 12 and f_numero == 909:
    print("CONTESTAR LLAMADA")
elif hora >= 17 and hora <= 19 and i_numero == 877:
    print("CONTESTAR LLAMADA")
elif hora >= 19 and hora <= 23:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")      