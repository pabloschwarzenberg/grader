#Cálculo del dígito verificador de un rut
numero_rut = list(reversed(input()))
serie = 2
sumatoria = 0

for numero in numero_rut:
    if serie == 8:
        serie = 2
    else:
        serie = serie

    sumatoria = sumatoria + (int(numero) * serie)
    serie += 1

    modulo_sumatoria = sumatoria % 11
    resultado_final = 11 - modulo_sumatoria 

if resultado_final == 11:
    dg_verificador = 0
elif resultado_final == 10:
    dg_verificador = "k"
else:
    dg_verificador = resultado_final

print("dv=",dg_verificador)
