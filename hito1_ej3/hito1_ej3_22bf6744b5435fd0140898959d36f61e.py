Ingreso=int(input("Ingrese el monto en pesos de su ingreso: "))
Ano=int(input("Ingrese su año de nacimiento: "))
Hijos=int(input("¿Cuantos hijos tienes?: "))
Pertenencia=int(input("¿Hace cuantos años perteneces al banco?: "))
Estado=input("¿Soltero(S) o Casado(C)?: ")
Lugar=input("¿Donde vives?¿Campo(R)o Ciudad(U)?: ")

C=Estado
S=Estado
R=Lugar
U=Lugar

if Pertenencia>10 and Hijos>=2:
    print("APROBADO")

elif Estado==C and Hijos>3 and 1973<Ano<1963:
    print("APROBADO")

elif Ingreso>2500000 and Estado==S and Lugar==U:
    print("APROBADO")

elif Ingreso>3500000 and Pertenencia>5:
    print("APROBADO")

elif Lugar==R and Estado==C and Hijos<2:
    print("APROBADO")

else:
    print("RECHAZADO")
    
      