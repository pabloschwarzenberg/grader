#Cálculo del dígito verificador de un rut
rut = (input("Inserte su rut sin puntos, guion ni digito verificador:"))
multiplos = 2
resultado_multiplicacion = 0

lista = []
for n in rut:
    lista.append(n)

limite = len(lista) - 1
while (limite >= 0):
    resultado_multiplicacion = (int(lista[limite]) * multiplos) + resultado_multiplicacion
    limite -= 1
    multiplos += 1
    if multiplos > 7:
        multiplos = 2

resultado_divison = int(resultado_multiplicacion)  / 11
resultado_total = int(resultado_multiplicacion) - (11 * int(resultado_divison))
final = (11 - resultado_total)
if final == 10:
    final = "k"
elif final == 11:
    final = 0
print("dv=",final)
