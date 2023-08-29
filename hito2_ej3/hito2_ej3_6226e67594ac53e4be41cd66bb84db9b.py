s = input('Ingrese una linea de texto a estudiar: ')
n = int(input('Ingrese un numero entero: '))

unicostring = []
conteostring = {}

for i in range(len(s) - n + 1):
    substr = s[i:i+n]

    if substr in conteostring:
        conteostring[substr] += 1
    else:
        conteostring[substr] = 1

for substr, count in conteostring.items():
    if count == 1:
        unicostring.append(substr)

if len(unicostring) == 0:
    print('ninguna')
else:
    print('Substrings Unicos de largo', n, 'en el texto:')
    for substr in unicostring:
        print(substr)