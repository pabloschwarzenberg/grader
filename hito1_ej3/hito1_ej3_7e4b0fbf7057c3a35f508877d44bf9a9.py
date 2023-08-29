#Aprobación de créditos
ing=int(input("¿cual es su ingreso(en pesos)?: "))
an=int(input("ingrese su año de nacimiento: "))
nh=int(input("¿cuantos hijos tiene?: "))
apb=int(input("ingrese el año de pertenencia en el banco: "))
ec=input("¿es soltero (s) o casado (C)?: ").lower()
cc=input("¿vive en campo (r) o ciudad (u)?: ").lower()
edad=2018-nh
if apb > 10 and nh >= 2:
    print("APROBADO")
elif ing>2500000 and ec=='s' and cc=="u":
    print("APROBADO")
elif ing>3500000 and apb>5:
    print("APROBADO")
elif cc=="r" and ec=="c" and nh<2:
    print("APROBADO")
elif ec=="c" and nh>3 and (edad<=55 and edad >= 45):
    print("APROBADO")
else:
    print("RECHAZADO")
