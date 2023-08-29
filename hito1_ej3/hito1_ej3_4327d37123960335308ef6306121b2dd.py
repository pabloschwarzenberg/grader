#Aprobación de créditos
I=int(input("Ingresos (en pesos):"))
AN=int(input("Ingrese su año de nacimiento:"))
NH=int(input("Ingrese su número de hijos:"))
AP=int(input("¿Hace cuántos años pertenece a este banco?"))
EC=str(input("Estado civil (S=Soltero, C=Casado):"))
RS=str(input("Lugar de residencia (U=Urbano, R=Rural):"))
if ((AP>10 and NH>=2) or (EC=="C" and NH>3 and 45<(2018-AN)<55) or (I>2500000 and EC=="S" and RS=="U") or (I>3500000 and AP>5) or (RS=="R" and EC=="C" and NH<2)):
    print("APROBADO")
else:
    print("RECHAZADO")