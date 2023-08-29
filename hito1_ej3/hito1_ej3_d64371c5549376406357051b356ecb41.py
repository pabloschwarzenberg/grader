#Aprobación de créditos
ingresos=int(input("ingreso mensual:"))
a_n=int(input("año de nacimiento:"))
hijos=int(input("cantidad de hijos:"))
a_banco=int(input("años de pertenencia en el banco:"))
estadoCivil=str(input("estado civil soltero(S) o casado(C):"))
campo_o_ciudad=str(input("campo(R) o ciudad(U):"))

edad=(2018)-(a_n)

while True :
    if a_banco>10 and hijos>2:
        print("APROBADO")
        break
    elif estadoCivil=="C" and hijos>3 and edad>=45<=55:
        print("APROBADO")
        break
    elif ingresos>2500000 and estadoCivil=="S" and campo_o_ciudad=="U":
        print("APROBADO")
        break
    elif ingresos>3500000 and a_banco>5:
        print("APROBADO")
        break
    elif campo_o_ciudad=="R" and estadoCivil=="C" and hijos<2:
        print("APROBADO")
        break
    else:
        print("RECHAZADO")
        break

