#Aprobación de créditos
ingr=int(input("Ingrese su ingreso en pesos: "))
anac=int(input("Ingrese su año de nacimiento: "))
nhij=int(input("Ingrese su número de hijos/as: "))
aper=int(input("Ingrese la cantidad de sus años de pertenencia al banco: "))
esci=str(input("Ingrese su estado civil (S = Soltero, C = Casado): ")).lower()
vive=str(input("Ingrese la región de su residencia ('U' = Urbano, 'R' = Rural): ")).lower()

ano=int(2020)
edad=int(ano-anac)

if aper>10 and nhij>=2:
    print("APROBADO")
elif esci=="c" and nhij>3 and edad>=45 and edad<=55:
    print("APROBADO")
elif ingr>2500000 and esci=="s" and vive=="u":
    print("APROBADO")
elif ingr>3500000 and aper>5:
    print("APROBADO")
elif vive=="r" and esci=="c" and nhij<2:
    print("APROBADO")
else:
    print("RECHAZADO") 