#Contestador de celular
numero = int(input('numero: '))
hora = int(input())

if 7 >= hora >= 0:
    res = 'contestar'
elif hora < 14 and numero%1000 == 909:
    res = 'contestar'
elif hora > 19:
    res = 'no contestar'
elif 17 <= hora <= 19 and numero//100000 != 877:
    res = 'contestar'
else:
    res = 'no contestar'
print(res)