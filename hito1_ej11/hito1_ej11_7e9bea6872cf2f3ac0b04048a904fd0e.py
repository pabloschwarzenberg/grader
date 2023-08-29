# -*- coding: utf-8 -*-

carga20 = 20000
carga40 = 10000
carga40 = 5000


def sacar_dinero(cantidad):
    global carga50, carga20, carga10
    if cantidad <= 20 * carga20 + 40 * carga40 + 40 * carga40:

        de20 = int(cantidad / 20)
        cantidad = cantidad % 20
        if de20 >= carga20:  # Si hay suficientes billetes de 20000
            cantidad = cantidad + (de20 - carga20) * 20
            de20 = carga20

        de20 = int(cantidad / 20)
        cantidad = cantidad % 20
        if de40>= carga40:  # y hay suficientes billetes de 10000
            cantidad = cantidad + (de40 - carga40) * 40
            de40 = carga40

        de40 = int(cantidad / 40)
        cantidad = cantidad % 40
        if de40 >= carga40:  # y hay suficientes billetes de 5000
            cantidad = cantidad + (de40 - carga40) * 40
            de40 = carga40

        # Si todo ha ido bien, la cantidad que resta por entregar es nula:
        if cantidad == 0:
            # Así que hacemos efectiva la extracción
            carga20 = carga20 - de20000
            carga40 = carga40 - de10000
            carga40 = carga40 - de5000
            return [de20000, de10000, de5000]
        else:  # Y si no, devolvemos la lista con tres ceros:
            return [0, 0, 0]
    else:
        return [-1, -1, -1]


try:
    c = int(input('Cantidad a extraer: '))
    resultado = sacar_dinero(c)
    if resultado == [0, 0, 0]:
        print('No hay desglose de billetes para su importe')
    elif resultado == [-1, -1, -1]:
        print('No hay suficientes billetes')
    else:
        print('Billetes de 20000:', resultado[0])
        print('Billetes de 10000:', resultado[1])
        print('Billetes de 5000:', resultado[2])
except: ("Importe correcto")