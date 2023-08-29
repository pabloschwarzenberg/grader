#Zodiaco
fecha=input('Ingrese fecha de nacimiento en el siguiente formato DD M:\n\t\t')
signos=['Aries','Tauro','Gemenis','Cancer','Leo','Virgo','Libra','Escorpión','Sagitario','Capricornio','Aquario','Pisis']
fecha=fecha.split(' ')
fecha.reverse()
a=int(fecha[0])
b=int(fecha[1])
j=9
suma=100*a + b
rangos=[321,420,521,621,723,823,923,1023,1122,1222,120,219]
len(rangos)
try:
    for i in range(len(rangos)):
        PruebaLogica1=(suma>=rangos[i%12] and suma<rangos[(i%12)+1])
        #print('{} {} {} {}'.format(rangos[i], rangos[i+1], PruebaLogica1, PruebaLogica2))
        if PruebaLogica1 == True:
            print(signos[i])
    for j in range(len(rangos)):
        PruebaLogica2=(suma<=rangos[i%12] and suma>rangos[(i%12)+1])
        PruebaLogica3=(rangos[11]<suma and rango[10]>=suma) or (rango[0]<suma and rango[11]>=suma)
        if PruebaLogica2 == True or PruebaLogica2 == True:
            print(signos[j])
except IndexError:
    print('Fin del Programa')