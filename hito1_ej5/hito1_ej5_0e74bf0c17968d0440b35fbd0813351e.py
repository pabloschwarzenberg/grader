#Cálculo del dígito verificador de un rut
      
#Ingreso de datos

rut = input("Ingresa el rut: ")

#Operacion

if not rut:
    print("Error: El rut  no puede estar vacío.")
    exit()

for digito in rut:
    if not digito.isdigit():
        print("Error: El RUT debe contener solo dígitos numéricos.")
        exit()

suma = 0
multiplicador = 2

for i in range(len(rut)-1, -1, -1):
    digito = int(rut[i])
    suma += digito * multiplicador
    multiplicador = multiplicador + 1 if multiplicador < 7 else 2

resto = suma % 11
dv = 11 - resto if resto != 0 else 0

#Resultado

print("dv =", dv)



