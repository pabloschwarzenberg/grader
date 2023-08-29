#Aprobación de créditos
ingreso = int(input(" especifique su ingreso: "))
anoNacimiento = int(input(" ingrese su año de nacimiento: "))
hijos = int(input(" ingrese su numero de hijos: "))
pertenenciaAlBanco = int(input(" ingrese sus años de pertenencia al banco: "))
estadoCivil = "A"
zona = "A"
anno = 2021 - anoNacimiento

while (estadoCivil != "S" and estadoCivil != "C"):
    estadoCivil = str(input(" ingrese si es soltero o casado con una S o una C respectivamente "))
while (zona != "U" and zona != "R"):
    zona = str(input(" ingrese si vive en zona urbana o rural con una U o R respectivamente "))

if (pertenenciaAlBanco >= 10 and hijos >= 2):
    print("APROBADO")
elif (estadoCivil == "C" and hijos >= 3 and anno >= 45 and anno <=55):
    print("APROBADO")
elif(ingreso >= 2500000 and estadoCivil == "S" and zona == "U"):
    print("APROBADO")
elif (ingreso >= 3500000 and pertenenciaAlBanco > 5):
    print("APROBADO")
elif (zona == "R" and estadoCivil == "C" and hijos < 2):
    print("APROBADO")
else:
    print("NO APROBADO")   