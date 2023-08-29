#aprobacion de credito
rural = ['r']
urbano = ['u']
casado = ['c']
soltero = ['s']

i = int(input("Ingreso en clp: "))
fn = int(input("Año de nacimiento: "))
nh = int(input("Numero de hijos: "))
ab = int(input("Años de pertenencia al banco: "))
es = input("Estado civil: s: 'soltero', c:'casado': ")
v = input("Si vive en campo o ciudad: u: 'urbano', r:rural': ")

if ab > 10 and nh >= 2:
    print("APROBADO")
elif es in casado and nh > 3 and 1965 <= fn <= 1975:
    print("APROBADO")
elif i > 2500000 and es in soltero and v in urbano:
    print("APROBADO")
elif i > 3500000 and ab > 5:
    print("APROBADO")
elif v in rural and es in  casado and nh < 2:
    print("APROBADO")
else: print("NO APROBADO")