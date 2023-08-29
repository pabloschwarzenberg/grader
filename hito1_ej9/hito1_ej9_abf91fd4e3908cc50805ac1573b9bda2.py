#Sistema de Ecuaciones
Xprimera=float(input("Ingresar valor de X en la primera ecuación"))
Yprimera=float(input("Ingresar valor de Y en la primera ecuación"))
Cprimera=float(input("Ingresar la la constante de la primera ecuación"))

Xsegunda=float(input("Ingresar valor de X en la segunda ecuación"))
Ysegunda=float(input("Ingresar valor de Y en la segunda ecuación"))
Csegunda=float(input("Ingresar la la constante de la segunda ecuación"))


if Xprimera != Xsegunda:
    XprimeraN=Xsegunda
    YprimeraN=Yprimera*Xsegunda/Xprimera
    CprimeraN=Cprimera*Xsegunda/Xprimera

#Entonces X son iguales, reemplazar una sobra la otra, quedara la funcion:

    y=(Csegunda-CprimeraN)/(Ysegunda-YprimeraN)

    print("y=",y)

    x=(Csegunda-Ysegunda*y)/Xsegunda

    print("x=",x)

if Xprimera == Xsegunda:

    y=(Csegunda-Cprimera)/(Ysegunda-Yprimera)

    print("y=",y)

    x=(Csegunda-Ysegunda*y)/Xsegunda

    print("x=",x)      