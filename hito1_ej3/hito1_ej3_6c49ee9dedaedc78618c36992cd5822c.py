#Aprobación de créditos
s = int(input("Ingrese su sueldo ($): "))
n = int(input("Año de nacimiento: "))
h = int(input("¿Cuantos hijos tiene?: "))
b = int(input("¿Hace cuantos años pertenece al banco?: "))
e = input("Soltero (s) o casado (c): ")
o = input("Urbano o rural: ")


if b > 10 and h >= 2:
    print("APROBADO")
else:
    if e == "C" and h > 3 and 1975<n<1985:
        print("APROBADO")
    else:
        if s > 2500000 and e == "S" and o == "U":
            print("APROBADO")
        else:
            if s > 3500000 and b > 5:
                print("APROBADO")
            else:
                if o == "R" and e == "C" and h < 2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")      