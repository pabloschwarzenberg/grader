#Cálculo del dígito verificador de un rut
rut = input("Ingrese el RUT (sin puntos ni guión): ") 

suma = 0
multiplicador = 2

 # Calcular la suma del producto de cada dígito por la serie
for digito in reversed(rut):
    suma += int(digito) * multiplicador
    if multiplicador < 7:
        multiplicador = multiplicador + 1
    else:
        multiplicador = 2

resto = suma - (suma // 11) * 11
digito_verificador = 11 - resto

if digito_verificador == 11:
    digito_verificador = 0
elif digito_verificador == 10:
    digito_verificador = "K"
    
print(f"Digito verificador: {digito_verificador}\nRut: {rut}-{digito_verificador}")

 