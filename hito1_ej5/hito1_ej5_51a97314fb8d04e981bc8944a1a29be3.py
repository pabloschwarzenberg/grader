#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese un rut sin digito verificador: "))
serie = "234567"

posicionRut = 0
posicionSerie = 0
suma = 0

while (rut > 0):
    suma = suma + ((rut % 10) * int(serie[posicionSerie]))
    rut = rut // 10
    if (posicionSerie < 5):
      posicionSerie = posicionSerie + 1
    else:
      posicionSerie = 0
  
dv = 11 - (suma % 11)

if (dv == 11):
  dv = 0
elif (dv == 10):
  dv = "K"

print("dv=", dv)
