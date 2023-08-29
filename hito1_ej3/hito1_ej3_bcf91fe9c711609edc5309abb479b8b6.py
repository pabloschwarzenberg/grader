#Aprobación de créditos
a = int(input("Ingreso (en pesos): "))
b = int(input("Año de nacimiento: "))
c = int(input("Numero de hijos: "))
d = int(input("Años de pertenencia al banco: "))
e = input("Estado civil: ")
f = input("Vive en campo o ciudad: ")
if d > 10 and c >= 2:
    print("APROBADO")
else:
    if e=="C" and c > 3 and 1965 <= b <= 1975:
        print("APROBADO")
    else:
        if a > 2500000 and e == "S" and f == "U":
            print("APROBADO")
        else:
            if a > 3500000 and d > 5:
                print("APROBADO")
            else:
                if f == "R" and e == "C" and c == (0 or 1):
                    print("APROBADO")
                else:
                    print("RECHAZADO")