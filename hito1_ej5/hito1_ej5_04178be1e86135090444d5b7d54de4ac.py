#Cálculo del dígito verificador de un rut
numero_rut = input("rut: ")
rut_reverso =numero_rut[::-1]
multiplicador = 2 #int = numero entero
suma = 0
for digito_del_rut in rut_reverso: #digito_del_rut = letra = string = str() ##toma 1 digito del rut reverso 
    suma = suma + (int(digito_del_rut) * multiplicador)
    multiplicador = multiplicador + 1 #multiplicador aumentara en +1 partiendo desde el 2
    if multiplicador == 8:
        multiplicador = 2
resto = suma//11
producto = resto * 11
sub_digito = suma - producto 
digito = 11 - sub_digito 
if digito == 11:
    digito = 0
elif digito == 10:
    digito = "K"
print("dv=" + str(digito))