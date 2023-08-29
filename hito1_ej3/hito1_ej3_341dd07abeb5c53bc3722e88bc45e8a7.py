a=float(input("Ingrese su Ingreso(en pesos): "))
b=float(input("ingrese su año de nacimiento: "))
c=float(input("Ingrese número de hijos: "))
d=float(input("Ingrese la cantidad de años de pertenencia al banco: "))
e=str(input("Ingrese su estado Civil(""S"": soltero, ""C"", casado): "))
f=str(input("Ingrese su localiad Campo o cuidad (""U"": urbano, ""R"": rural): "))


if d>=10 and c>=2 :
    print("APROBADO")
else:
    if e== "C"or"c" and c>3 and 45<=(b-2021)<=55:
        print("APROBADO")
    else:
        if a >=2500000 and e== "s"or"S" and f== "u"or "U":
            print("APROBADO")
        else:
            if a>=3500000 and d> 5:
                print("APROBADO")
            else:
                if f== "r"or "R" and e== "c"or "C" :
                    print("APROBADO")
                else:
                    print("RECHAZADO")
