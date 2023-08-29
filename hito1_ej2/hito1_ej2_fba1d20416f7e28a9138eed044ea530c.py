#Contestador de celular
x = int(input('¿Qué número realizó la llamada? ')[:8])
print(x)
y = int(input('¿A qué hora fue la llamada? ')[:2])
print(y)

if y >= 0 and y <= 7:
    print('CONTESTAR')
elif y < 14 and x%1000 == 909:
    print('CONTESTAR')
elif y >= 17 and y <= 19 and x//100000 != 877:
    print('CONTESTAR')
else:
    print('NO CONTESTAR')