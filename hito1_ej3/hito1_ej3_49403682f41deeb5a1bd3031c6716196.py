#Aprobación de créditos
print("Por favor menciona los siguentes datos")

ingreso = int(input("Ingreso (en pesos) : "))
edad = int(input("Cual es su edad : "))
hijos = int(input("Numeros de hijos : "))
banco = int(input("Años de pertenencia al banco : "))
estado = str(input('S'":soltero,'C' : casado : "))
vivienda = str(input("Si vive en campo o ciudad ('U':urbano,'R':rural) :"))
Aprobacion = " "

if banco > 10:
    if hijos > 2:
        Aprobacion = 'APROBADO'

elif estado == 'C':
    if hijos > 3:
        if edad <= 1977 or edad >= 1967:
            Aprobacion = 'APROBADO'

elif ingreso > 2500000:
    if estado == 'S':
        if vivienda == 'U':
            Aprobacion = 'APROBADO'

elif ingreso > 3500000:
    if banco >= 5:
        Aprobacion = 'APROBADO'

elif estado == 'C':
    if vivienda == 'R':
        if hijos >= 2:
            Aprobacion = 'APROBADO'
elif ingreso <= 450000:
    if edad >= 1970:
        if hijos <= 1:
         if banco >= 11:
             if estado == 'C' :
                 if vivienda == 'R':
                     print(Aprobacion)

print(Aprobacion)
