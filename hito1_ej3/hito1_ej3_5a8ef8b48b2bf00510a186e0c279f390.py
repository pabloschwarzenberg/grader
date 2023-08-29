# Aprobacion de Creditos
#Encabezado y solicitud de info por teclado

ing = int(input("Ingreso (en pesos): "))
nac = int(input("Año de nacimiento: "))
hijos = int(input("Número de hijos: "))
años = int(input("Años de pertenencia al banco: "))
civil = str(input("Estado civil ('S': Soltero, 'C':Casado): "))
casa = str(input("Lugar donde habita ('U': Urbano, 'R':Rural): "))

#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if años > 10 and hijos >= 2:
    print("APROBADO")
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
    if civil == "C" and hijos >= 3 and (2021 - nac) >=45 and (2021 - nac) <= 55:
        print("APROBADO")
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y
#vive en la ciudad.
    if ing >2500000 and civil == "C" and casa == "U":
        print("APROBADO")
#Si el ciente tiene ingresos superiores a $3.500.000 y
#pertenece al banco por más de 5 años
    if ing > 3500000 and años > 5:
        print("APROBADO")
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
    if casa == "R" and civil == "C" and hijos < 2:
        prit("APROBADO")
else:
    print("NO APROBADO")
