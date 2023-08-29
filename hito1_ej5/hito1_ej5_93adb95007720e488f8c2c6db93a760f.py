#Cálculo del dígito verificador de un rut
def digito_verificador(rut):
    value = 11 - sum([ int(a)*int(b)  for a,b in zip(str(rut).zfill(8), '32765432')])%11
    return {10: 'K', 11: '0'}.get(value, str(value))
x = int(input("Ingrese su rut: "))
print("dv=" + digito_verificador(x))