#Aprobación de créditos
sueldo = int(input("ingrese cantidad de sueldo liquido: "))
año = int(input("año nacimiento: "))
numhij = int(input("ingrese numero de hijos: "))
añosbanco = int(input("años en banco: "))
estciv = str(input("estado civil (S para soltero, C para casado): "))
res = str(input("lugar donde reside (considere U para urbano y R para rural): "))
R = "R"
U = "U"
S = "S"
C = "C"
if añosbanco > 10:
    if numhij >= 2 :
        print("APROBADO")
    else:
        if res == R:
            if estciv == C:
                print("APROBADO")
            else:
                print("RECHAZADO")
        else:
            print("RECHAZADO")
else:
    if estciv == C:
        añoscumplidos = eval(input("cumplio años el presente año : "))
        if añoscumplidos == si:
            añosc = 2020 - (año + 1)
            if 45 <= añosc <= 55:
                if numhij > 3 :
                    print("APROBADO")
                else:
                    print("RECHAZADO")
        else:
            añosn = 2020 - año
            if 45 <= añosn <= 55:
                if numhij > 3:
                    print("APROBADO")
                else:
                    print("RECHAZADO")
            else:
                print("RECHAZADO")
    else:
        if sueldo > 2500000:
            if estciv == S:
                if res == U:
                    print("APROBADO")
                else:
                    print("RECHAZADO")
            else:
                print("RECHAZADO")
        else:
            if sueldo > 3500000:
                if añosbanco > 5:
                    print("APROBADO")
                else:
                    print("RECHAZADO")      