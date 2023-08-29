#Aprobación de créditos
a=int(input("Declare Ingresos:"))
b=int(input("Año de nacimiento:"))
c=int(input("Número de hijos:"))
d=int(input("Años de pertenencia al banco:"))
e=input("Estado civil:")
f=input("Zona de residencia:")
if(10<d):
    if(2<=c):print("APROBADO")
    else:
        if(e=="C"):
         if(3<c):
            if(1961<=b<=1971):print("APROBADO")
            else:print("RECHAZADO")
         else:
            if(f=="R"):
                if(c<2):print("APROBADO")
                else:print("RECHAZADO")
            else:print("RECHAZADO")
        else:
         if(2500000<a):
            if(e=="S"):
                if(f=="U"):print("APROBADO")
                else:print("RECHAZADO")
            else:
                if(3500000<a):
                    if(5<d):print("APROBADO")
                    else:print("RECHAZADO")
                else:print("RECHAZADO")
         else:print("RECHAZADO")
else:
    if(e=="C"):
        if(3<c):
            if(1961<=b<=1971):print("APROBADO")
            else:print("RECHAZADO")
        else:
            if(f=="R"):
                if(c<2):print("APROBADO")
                else:print("RECHAZADO")
            else:print("RECHAZADO")
    else:
        if(2500000<a):
            if(e=="S"):
                if(f=="U"):print("APROBADO")
                else:print("RECHAZADO")
            else:
                if(3500000<a):
                    if(5<d):print("APROBADO")
                    else:print("RECHAZADO")
                else:print("RECHAZADO")
        else:print("RECHAZADO")

