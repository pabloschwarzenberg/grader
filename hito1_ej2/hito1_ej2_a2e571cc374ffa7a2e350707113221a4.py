# Contestador de celular
numero = int(input())
hora = int(input())
if 0 <= hora <= 7:
    result = "CONTESTAR"
elif 7 < hora <= 14:
    if int(numero % 1000) == 909:
        result = "CONTESTAR"
    else:
        result = "NO CONTESTAR"
elif 14 < hora < 17:
    result = "NO CONTESTAR"
elif 17 <= hora <= 19:
    if int(numero // 100000) == 877:
        result = "NO CONTESTAR"
    else:
        result = "CONTESTAR"
elif 19 < hora:
    result = "NO CONTESTAR"
print(result)
