rut =  input()
if len(rut) == 7:
    rut = "0"+rut
multiplicaciones = []
multiplicador = 3
for i in rut:
    resultado = int(i)*multiplicador
    multiplicaciones.append(resultado)
    multiplicador-=1
    if multiplicador == 1:
        multiplicador = 7
final = 0
for i in multiplicaciones:
    final += i
restar = int(final/11)
total = final-(restar*11)
digito = 11 - total
if digito == 11:
    digito = 0
if digito == 10:
    digito = "K"
print("dv="+str(digito))