Signos = ["acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario", "capricornio"]
Fechas = [20, 19, 21, 20, 21, 21, 23, 23, 23, 22, 22, 21]
dia = int(input("Digite su día de cumpleaños como número: "))
mes = int(input("Digite su mes de nacimiento como número: "))

if dia >= Fechas[mes - 1]:
    mes = mes - 1

print(Signos[mes])