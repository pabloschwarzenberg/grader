#Zodiaco

dia = int(input('ingrese dia: '))
mes = int(input('Ingrese mes: '))

fecha_transicion = [20 , 19 , 21 , 20 , 21 , 21 , 23 , 23 , 23 , 23 , 22 , 22]  #DETALLE IMPORTANTE: ESTA ORDENADO DE ENERO A DICIEMBRE
signos = ['capricornio','acuario','piscis','aries','tauro','geminis','cancer','leo','virgo','libra','escorpio','sagitario'] #DETALLE IMPORTANTE: ESTA OREDNADO DE ENERO A DICIEMBRE

mes=mes-1  #LE RESTAMOS 1 PARA PODER MOVERNOS A TRAVES DE LA LISTA CORRECTAMENTE

if dia>fecha_transicion[mes]:       #En el caso de que el dia sea mayor a la fecha de transicion entonces suponemos que la persona nacio el mes siguiente
    mes=mes+1

    if mes==12:                     #En el caso en que la persona haya nacido despues de la fecha de transicion y en diciembre, supondremos que la persona nacio en enero
        mes = 0

print('tu signo es: ' + signos[mes])
