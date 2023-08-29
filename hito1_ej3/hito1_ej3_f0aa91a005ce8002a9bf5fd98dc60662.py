ingreso=int(input("cuanto gana oe: "))
ano_de_nacimiento=input("año de nacimiento: ")
ano_de_nacimiento=int(ano_de_nacimiento)
anos=2017-ano_de_nacimiento
numero_hijos=input("cuantos hijos tiene: ")
numero_hijos=int(numero_hijos)
anos_en_banco=input("años en el banco: ")
anos_en_banco=int(anos_en_banco)
estado_civil=input("casado(C) o soltero(S): ")
estado_civil=str(estado_civil)
reside=input("ciudad(U) o campo(R): ")
reside=str(reside)
C=True
R=True
if anos_en_banco>10 and numero_hijos>=2:
 print("APROBADO")
elif estado_civil==C and numero_hijos>3 and 45<anos<55:
 print("APROBADO")
elif ingreso>2500000 and estado_civil==S and reside==U:
 print("APROBADO")
elif ingreso>3500000 and anos_en_banco>5:
 print("APROBADO")
elif reside==R and estado_civil==C and numero_hijos<2:
 print("APROBADO")
else:
 print("APROBADO")
