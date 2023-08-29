# Pedir al usuario que ingrese un número que represente un rut
rut = int(input("Ingrese un número que represente un rut: "))

# Inicializar una variable para almacenar el dígito verificador
dv = 0

# Inicializar una variable para almacenar la suma de los productos
suma = 0

# Inicializar una variable para almacenar el factor de multiplicación
factor = 2

# Mientras el rut sea mayor que cero
while rut > 0:
  # Obtener el último dígito del rut
  digito = rut % 10
  # Multiplicar el dígito por el factor y agregarlo a la suma
  suma = suma + digito * factor
  # Aumentar el factor en uno
  factor = factor + 1
  # Si el factor es mayor que siete, volverlo a dos
  if factor > 7:
    factor = 2
  # Dividir el rut por diez y actualizarlo
  rut = rut // 10

# Calcular el resto de dividir la suma por once
resto = suma % 11

# Calcular el dígito verificador usando la fórmula 11 - resto
dv = 11 - resto

# Si el dígito verificador es diez, asignarle la letra K
if dv == 10:
  dv = "K"
# Si el dígito verificador es once, asignarle el cero
elif dv == 11:
  dv = 0

# Imprimir el dígito verificador
print("dv=" + str(dv))
