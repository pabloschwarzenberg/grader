ingreso = int(input("ingrese la cantidad de sus ingresos :"))
anno_nacimiento = int(input("año de nacimiento : "))
hijos = int(input("ingrese el numero de hijos : "))
annos_en_banco = int(input("cantidad de años n banco :"))
estado_civil = str(input("estado civil (S para soltero, C para casado) : "))
vive = str(input("lugar de residencia (considere U para urbano y R para rural) : "))
R = "R"
U = "U"
S = "S"
C = "C"
if annos_en_banco > 10:
    if hijos >= 2 :
        print("APROBADO")
    else:
        if vive == R:
            if estado_civil == C:
                print("APROBADO")
            else:
                print("RECHAZADO")
        else:
            print("RECHAZADO")
else:
    if estado_civil == C:
        annos_cumplidos = eval(input("cumplio años el presente año : "))
        if annos_cumplidos == si:
            annosc = 2020 - (anno_nacimiento + 1)
            if 45 <= annosc <= 55:
                if nh > 3 :
                    print("CREDITO APROBADO")
                else:
                    print("CREDITO RECHAZADO")
        else:
            annosn = 2020 - anno_nacimiento
            if 45 <= annosn <= 55:
                if nh > 3:
                    print("CREDITO APROBADO")
                else:
                    print("CREDITO RECHAZADO")
            else:
                print("CREDITO RECHAZADO")
    else:
        if ingreso > 2500000:
            if estado_civil == S:
                if vive == U:
                    print("CREDITO APROBADO")
                else:
                    print("CREDITO RECHAZADO")
            else:
                print("CREDITO RECHAZADO")
        else:
            if ingreso > 3500000:
                if annos_en_banco > 5:
                    print("CREDITO APROBADO")
                else:
                    print("CREDITO RECHAZADO")
          