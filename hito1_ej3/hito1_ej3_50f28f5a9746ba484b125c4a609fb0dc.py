from os import system
system("cls")
print("Bienvenido a su banco, ingrese los siguientes datos:")
while True:
    ing=input("Su Ingreso (en pesos): ")
    if ing.isdigit:
        ing1=int(ing)
        break
    else:
        print("Ingrese un valor valido")
while True:
    nac=input("Su Año de nacimiento: ")
    if nac.isdigit:
        nac1=int(nac)
        edad=2023-nac1
        break
    else:
        print("Ingrese un valor valido")
while True:
    hij=input("El número de hijos que tiene: ")
    if hij.isdigit:
        hij1=int(hij)
        break
    else:
        print("Ingrese un valor valido")
while True:
    pert=input("Los años de pertenencia al banco: ")
    if pert.isdigit:
        pert1=int(pert)
        break
    else:
        print("Ingrese un valor valido")
while True:
    Est=input("Estado civil (S: soltero, C, casado): ").lower()
    if Est=="s" or Est=="c":
        break
    else:
        print("Ingrese un valor valido")
while True:
    viv=input("Si vive en campo o cuidad (U: urbano, R: rural): ").lower()
    if viv=="u" or viv=="r":
        break
    else:
        print("Ingrese un valor valido")


if pert1>=10 and hij1>=2:
    print("APROBADO")
elif Est=="c" and hij1>3 and edad>=45 and edad<=55:
    print("APROBADO")
elif ing1>=2500000 and Est=="s" and viv=="u":
    print("APROBADO")
elif ing1>=3500000 and pert1>=5:
    print("APROBADO")
elif viv=="r" and Est=="c" and hij1<2:
    print("APROBADO")
else:
    print("RECHAZADO")