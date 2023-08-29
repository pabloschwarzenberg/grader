#Contestador de celular
cel = input()
hora = int(input())

if 0 <= hora <= 7:
    resultado = 'CONTESTAR'
elif 7 < hora < 14 and cel[5:8] == '909':
    resultado = 'CONTESTAR'
elif 17 < hora < 19 and cel[:3] != '877':
    resultado = 'CONTESTAR'
else:
    resultado = 'NO CONTESTAR'

print(resultado)      