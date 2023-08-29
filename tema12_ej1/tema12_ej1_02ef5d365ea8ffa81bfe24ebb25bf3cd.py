def generador_binario(largo):
    lista = []
    if largo == 1:
        lista += ['0','1']
    else:
        lista_temp = generador_binario(int(largo)-1)
        for i in lista_temp:
            lista.append('0' + i)
        for i in lista_temp:
            lista.append('1' + i)
    return lista

largo = input()

for i in generador_binario(largo):
    print(i)
