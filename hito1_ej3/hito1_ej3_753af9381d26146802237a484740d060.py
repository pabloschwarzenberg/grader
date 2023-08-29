#Aprobación de créditos
print("Hola, si tus intenciones son postular a un crédito en este banco, por favor ingresa los siguientes datos")
soltero = 0
casado = 0
urbana = 0
rural = 0
ingresos = 0
Ano_nacimiento = 0
Numero_hijos = 0
Anos_afiliacion = 0
S = soltero
C = casado
Estado_civil = S or C
U = urbana
R = rural
Vivienda = U or R
ingresos = eval(input("¿A cuánto corresponde su ingreso en pesos?: "))
Ano_nacimiento = eval(input("¿En qué año nació?: "))
Numero_hijos = eval(input("¿Cuántos hijos tiene? :"))
Anos_afiliacion = eval(input("¿Cuántos anos lleva perteneciendo al banco?: "))
Estado_civil = eval(input("Ingrese su actual estado civil, indicando con S si se encuentre soltero o indicando con C si se encuentra casado: "))
Vivienda = eval(input("Indique con U si vive en área urbana o indique con R si vive en área rural: "))
if(Anos_afiliacion > 10) and (2 <= Numero_hijos):
  print("APROBADO")
elif(Estado_civil == C) and (3 < Numero_hijos) and (Ano_nacimiento <= 1966) and (Ano_nacimiento >= 1976):
  print("APROBADO")
elif(ingresos > 2500000) and (Estado_civil == S) and (Vivienda == U):
  print("APROBADO")
elif(ingresos > 3500000) and (Anos_afiliacion > 5):
  print("APROBADO")
elif(Vivienda == R) and (Estado_civil == C) and (Numero_hijos <= 2):
  print("APROBADO")
else:
  print("RECHAZADO")
