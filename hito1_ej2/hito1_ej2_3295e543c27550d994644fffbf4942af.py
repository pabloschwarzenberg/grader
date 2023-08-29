#entrada
nc_int = int(input("Ingrese numero celular de 8 digitos: "))
hl = int(input("Ingrese hora de llamada: "))

#procedimiento

nc = str(nc_int)
len(nc)

if (hl >= 0 and hl <= 7):
    print("CONTESTAR")
elif (hl < 14 and "909" in nc[5:8]):
    print("CONTESTAR")
elif (hl < 14):
    print("NO CONTESTAR")
elif (hl >= 17 and hl <= 19 and "877" in nc[0:3]):
    print("NO CONTESTAR")
elif (hl >=17 and hl <=19):
    print("CONTESTAR")
elif (hl > 19):
    print("NO CONTESTAR")
else:
    print()