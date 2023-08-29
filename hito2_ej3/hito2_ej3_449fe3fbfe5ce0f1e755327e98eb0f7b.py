def adn_unico(x,n):
    x = x.lower()
    secciones = []
    for i in range(len(x)-n+1):
        secc = x[i:i+n]
        secciones.append(secc)
    k=0
    unicas = []
    while k<len(secciones):
        cant = secciones.count(secciones[k])
        if cant==1:
            unicas.append(secciones[k])
        k = k+1
    if len(unicas)==0:
        return 'ninguna'
    else:
        return unicas

secuencia = input('Ingrese la secuencia de ADN: ')
largo = int(input('Ingrese el largo del fragmento: '))
print(adn_unico(secuencia,largo))