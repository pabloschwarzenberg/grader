#Aprobación de créditos
ingreso_el_monto=eval(input("Ingrese Monto de ingreso_el_monto: "))
Nacimiento=int(input("Ingrese año de Nacimiento: "))
numero_de_hijos=int(input("Ingrese Cantidad de numero_de_hijos: "))
años_de_permanencia=int(input("Ingrese Años de años_de_permanencia: "))
Estado_civil=input("Ingrese Estado Civil : ")
vive_en_ciudad_o_campo=input("Ingrese Ciudad='U:Urbano' o Campo='R: rural : ")

Edad=2021-Nacimiento

if años_de_permanencia>10 and  numero_de_hijos>=2:
    print("APROBADO")
elif Estado_civil=='C' and numero_de_hijos>3 and Edad>=45 and Edad<=55:
    print("APROBADO")
elif ingreso_el_monto>2500000 and Estado_civil=='C' and vive_en_ciudad_o_campo=='U':
    print("APROBADO")
elif ingreso_el_monto>3500000 and años_de_permanencia>5:
    print("APROBADO")
elif vive_en_ciudad_o_campo=='R' and Estado_civil=='C' and numero_de_hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")      