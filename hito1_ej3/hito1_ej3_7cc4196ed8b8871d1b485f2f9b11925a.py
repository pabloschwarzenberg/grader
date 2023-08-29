#Aprobación de créditos
x = int(input("Ingreso(en pesos): "))
z = int(input("Año de nacimiento: "))
lista1 = [1966,1976,1]

c = int(input("Numero de hijos: "))
v = int(input("Años de pertenencia al banco: "))

b = str(input("Estado civil(S: soltero, C, casado): "))
def C ():
    b = C
def S ():
    b = S

n = str(input("Si vive en campo o cuidad (U: urbano, R: rural): "))
def U ():
    n = U
def R ():
    n = R

if v > 10 and  c >= 2:
    print("APROBADO")
else:
    if C and c > 3 and z == lista1:
        print("APROBADO")

    else:
        if x > 2500000 and S and U:
            print("APROBADO")
        else:
            if x > 3500000 and v > 5:
                print("APROBADO")
            else:
                if R and C and c < 2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")