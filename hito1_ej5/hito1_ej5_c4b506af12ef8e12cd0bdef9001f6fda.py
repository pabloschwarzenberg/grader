#Cálculo del dígito verificador de un rut
rut= eval (input ("rut "))
factores = "32765432"
indice = len(factores) -1
suma = 0 
while rut > 0:
digito = rut % 10 
suma = suma + (digito * int(factores[indice]))
rut = rut // 10 
indice = indice 
resto = suma % 11
dv = 11 - resto 
if dv == 10:
print ("dv = k")
else:
print ("dv = ", dv) 
