'''Escribe un programa que reciba como parámetro el día y el mes del cumpleaños de una persona (como números enteros) y que imprima el signo del zodíaco al que pertenece.

Para determinar las fechas de cada signo utiliza la columna Tropical Zodiac en la tabla de fechas que aparece en este link (Wikipedia).
Al ingresar 4 12 tu programa debe imprimir: sagitario
Al ingresar 27 3 tu programa debe imprimir: aries'''

Signos=['aries', 'tauro', 'gemenis', 'cancer', 'leo', 'virgo', 'libra', 'escorpio', 'sagitario', 'capricornio', 'acuario', 'piscis']
informacion=input('Ingresar mes y dia de cumpleaños (DD MM)\t')
informacion=(informacion.replace(' ','-')).split('-')
fechas=[[4,20],[5,21],[6,21],[7,23],[8,23],[9,23],[10,23],[11,22],[12,22],[1,20],[2,19],[3,21]]
for i in range(11):
    if int(informacion[1])==fechas[i][0]:
        if int(informacion[0])<=fechas[i][1]:
            print(Signos[i])
            break
        else:
            print(Signos[i+1])
            break