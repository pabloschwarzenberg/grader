Ingreso= int(input("Ingrese el Ingreso: "))
born=int(input("Ingrese el Año de nacimiento:"))
Nhijos=int(input("Ingrese el numero de hijos: "))
TiempoB=int(input("Ingrese los años en el banco: "))
EstadoC=(input("Ingrese el Estado Civil actual:"))
Vive=(input("Ingrese si habita en Campo o Ciudad: "))
edad= 2020 - born
if TiempoB > 10 and Nhijos >= 2:
    print("APROBADO")
else:
    if EstadoC == "C" and 45 <= edad<= 55:
        print("APROBADO")
    else:
        if Ingreso >= 2500000 and EstadoC == "S" and Vive == "U":
            print("APROBADO")
        else:
            if Ingreso > 3500000 and TiempoB > 5:
                print("APROBADO")
            else:
                if Vive == "R" and EstadoC == "C" and Nhijos < 2:
                    print("APROBADO")