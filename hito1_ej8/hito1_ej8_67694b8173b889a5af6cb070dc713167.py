#Descomponer un número
ingreso = int(input("Ingresa un numero: "))
ingreso_str = str(ingreso)
ingreso_lista = list(ingreso_str)

Unidades = ingreso_lista[-1] + str("U")


if ingreso < 10:
    print(Unidades)
elif ingreso < 100:
    Dece = ingreso_lista[-2] + str("D")
    print(Dece,"+",Unidades)
elif ingreso < 1000:
    Dece = ingreso_lista[-2] + str("D")
    Cente = ingreso_lista[-3] + str("C")
    print(Cente,"+",Dece,"+",Unidades)
elif ingreso < 10000:
    Dece = ingreso_lista[-2] + str("D")
    Cente = ingreso_lista[-3] + str("C")
    Miles = ingreso_lista[0] + str("M")
    print(Miles,"+",Cente,"+",Dece,"+",Unidades)
else:
    ("numero fuera de rango")

