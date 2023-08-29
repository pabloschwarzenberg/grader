#Cálculo del dígito verificador de un rut
rut = input("Ingrese rut sin puntos ni dígito verificador")

contador = 1
multiplicador = 2
suma = 0
largo = len(rut)

while contador <= largo:
  if multiplicador > 7: multiplicador = 2
  suma += int(rut[largo-contador])*multiplicador
  multiplicador += 1
  contador += 1
  
resto = suma%11  
digitoEntero = 11 - resto

if digitoEntero == 10: print("dv=k")
elif digitoEntero == 11: print("dv=0")
else: print("dv=", digitoEntero)

