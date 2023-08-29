#Aprobación de créditos
solterou=0
casadou=0
urbana=0
rural=0
ingresous=0
Ano_nacimientou=0
Numero_hijous=0
Anos_afiliacion=0
S = solterou
C = casadou
Estado_civil = S or C
U = urbana
R = rural
Vivienda = U or R
print("Hola, si quiere postular a un crédito en este bancou, ingrese los siguientes datous")
ingresous = eval(input("¿A cuántou corresponde su ingresou en pesous?: "))
Ano_nacimientou = eval(input("¿En qué añou nacióu?: "))
Numero_hijous = eval(input("¿Cuántous hijous tiene? :"))
Anos_afiliacion = eval(input("¿Cuántous añous lleva perteneciendo al bancou?: "))
Estado_civil = eval(input("Ingrese su actual estado civil, indicando con S si se encuentre solterou o indicando con C si se encuentra casadou: "))
Vivienda = eval(input("Indique con U si vive en área urbana o indique con R si es en área rural: "))
if(Anos_afiliacion > 10) and (2 <= Numero_hijous):
  print("APROBADO")
elif(Estado_civil == C) and (3 < Numero_hijous) and (Ano_nacimientou <= 1966) and (Ano_nacimientou >= 1976):
  print("APROBADO")
elif(ingresous > 2500000) and (Estado_civil == S) and (Vivienda == U):
  print("APROBADO")
elif(ingresous > 3500000) and (Anos_afiliacion > 5):
  print("APROBADO")
elif(Vivienda == R) and (Estado_civil == C) and (Numero_hijous <= 2):
  print("APROBADO")
else:
  print("RECHAZADO")      