#Aprobación de créditos
A =int(input("Ingresos (en pesos): "))
B =int(input("Año de Nacimiento: "))
C =int(input("Numero de Hijos: "))
D =int(input("Años de Pertenencia la banco: "))
E =str(input("Estado Civil( (S):Soltero, (C):Casado: "))
F =str(input("Si vive en el Campo o Ciudad( (U):Urbano, (R):Rural: "))

G =str(E[-1])
H =2020-B
I =str(F[-1])

if D>=10 and C>2:
    print("APROBADO")

elif (G==("C")) or (G==("c")) and (C>3) and (45<=H<=55):
    print("APROBADO")

elif (A>2500000) and (G==("S")) or (G==("s")) and (I==("U")) or (I==("u")):
    print("APROBADO")

elif (A>3500000) and (D>5):
    print("APROBADO")

elif (I==("R")) or (I==("r")) and  (G==("C")) or (G==("c")) and (C<2):
    print("APROBADO")

else:
    print("RECHAZADO")