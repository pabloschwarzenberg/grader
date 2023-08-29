sueldo=float(input("Ingrese se sueldo sin puntos: "))
nac=int(input("Ingrese AÑO de nacimiento: "))
hijos=int(input("Ingrese su numero de hijos: "))
antiguedad=float(input("Ingrese años de antiguedad: "))
estadocivil=input("Estado civil S para para soltero, C para casado: ").lower()
vive=input("Donde vive? U para urbano, R para rural: ").lower()
naci=2020-nac

#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.

if antiguedad > 10 and hijos >=2:
    print("APROBADO SU CREDITO")
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
elif naci > 44 and naci < 56:
    if estadocivil== "c" and hijos > 3:
        print("APROBADO SU CREDITO")
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif sueldo > (2500000) and estadocivil == "s":
    if vive == "u":
        print("APROBADO SU CREDITO")
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
elif sueldo > 3500000 and antiguedad > 5:
    print("APROBADO SU CREDITO")
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos
elif hijos <= 1 and vive == "r":
    print("APROBADO SU CREDITO")
else:
    print("RECHAZADO")
