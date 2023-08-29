d = int(input("ingrese la cantidad de su sueldo liquido :"))
año = int(input("año de nacimiento : "))
nh = int(input("ingrese el numero de hijos : "))
añosenbanco = int(input("cantidad de años n banco :"))
estado = str(input("estado civil (S para soltero, C para casado) : "))
residencia = str(input("lugar de residencia (considere U para urbano y R para rural) : "))
R = "R"
U = "U"
S = "S"
C = "C"
if añosenbanco > 10:
    if nh >= 2 :
        print("APROBADO")
    else:
        if residencia == R:
            if estado == C:
                print("APROBADO")
            else:
                print("RECHAZADO")
        else:
            print("RECHAZADO")
else:
    if estado == C:
        añoscumplidos = eval(input("cumplio años el presente año : "))
        if añoscumplidos == si:
            añosc = 2020 - (año + 1)
            if 45 <= añosc <= 55:
                if nh > 3 :
                    print("APROBADO")
                else:
                    print("RECHAZADO")
        else:
            añosn = 2020 - año
            if 45 <= añosn <= 55:
                if nh > 3:
                    print("APROBADO")
                else:
                    print("RECHAZADO")
            else:
                print("RECHAZADO")
    else:
        if d > 2500000:
            if estado == S:
                if residencia == U:
                    print("APROBADO")
                else:
                    print("RECHAZADO")
            else:
                print("RECHAZADO")
        else:
            if d > 3500000:
                if añosenbanco > 5:
                    print("APROBADO")
                else:
                    print("RECHAZADO")
         
      