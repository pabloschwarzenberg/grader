# Entrada de los Numeros
x = int(input("Ingrese primer numero: "))
y = int(input("Ingrese segundo numero: "))
z = int(input("Ingrese tercer Numero: "))

# Calculo de numeros de menor a mayor
if x > y and x > z:
    mayor = x
    if y > z:
        medio, menor = y, z
    else:
        medio, menor = z, y
if y > x and y > z:
    mayor = y
    if x > z:
        medio, menor = x, z
    else:
        medio, menor = z, x
elif z > x and z > y:
    mayor = z
    if x > y:
        medio, menor = x, y
    else:
        medio, menor = y, x

# Salida del Orden de Numeros 
print ( menor, "," , medio ,"," , mayor)
print ("Fin, aqui esta el orden de menor a mayor :)") 