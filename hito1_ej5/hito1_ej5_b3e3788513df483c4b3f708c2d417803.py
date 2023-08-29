#Cálculo del dígito verificador de un rut
rut = input("Ingrese el rut sin dígito verificador: ")
suma = 0
factor = 2

# Recorrer los dígitos del rut de derecha a izquierda
posicion = len(rut) - 1
while posicion >= 0:
  digito = int(rut[posicion])
  suma += digito * factor
  factor += 1
  if factor > 7:
      factor = 2
  posicion -= 1
  
# Calcular el dígito verificador
resto = suma % 11
if resto == 1:
    dv = "k"
elif resto == 0:
    dv = 0
else:
    dv = 11 - resto
  
print("dv=", dv)