secuencia1 = input('Ingrese la primera secuencia de ADN: ')
secuencia2 = input('Ingrese la segunda secuencia de ADN: ')
adn_alineado = ''
verificador_sec2 = 0

for caracter in secuencia1:
    if verificador_sec2 < len(secuencia2):
        if caracter == secuencia2[verificador_sec2]:
            adn_alineado += secuencia2[verificador_sec2]
            verificador_sec2 += 1
        else:
            adn_alineado += '_'
    else:
        adn_alineado += '_'

if verificador_sec2 < len(secuencia2):
    adn_alineado += secuencia2[verificador_sec2:]

print(adn_alineado)