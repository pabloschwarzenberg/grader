#Cálculo del dígito verificador de un rut
vector_rut = []
serie_numerica = [2, 3, 4, 5, 6, 7]
rut = input("Ingrese su rut sin codigo verificador: ")

for i in rut:
    vector_rut.append(i)
vector_rut.reverse()

suma_verificador = 0
contador_digitos = 0

for i in range(0, len(vector_rut)):
    if contador_digitos >= len(serie_numerica):
        contador_digitos = 0
    suma_verificador += int(vector_rut[i]) * int(serie_numerica[contador_digitos])
    contador_digitos += 1
mod_11 = 11 - (suma_verificador % 11)


if mod_11 == 11:
    print("dv=0")
elif mod_11 == 10:
    print("dv=k")
else:
    print("dv=" + str(mod_11))
