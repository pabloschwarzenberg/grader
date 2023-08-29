#Zodiaco
listaMeces = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

    

d = int(input('Ingrese el dia: '))
m = int(input('Ingrese el Mes: '))
mes = listaMeces[m-1]

if (mes == 'Marzo' and (d >=21 and d <= 31 )) or (mes == 'Abril' and (d >=1 and d <= 19)):
    print ('Aries')
    
elif (mes == 'Abril' and (d >=20 and d <= 30 )) or (mes == 'Mayo' and (d >=1 and d <= 20)):
    print('Tauro')

elif (mes == 'Mayo' and (d >=21 and d <= 31 )) or (mes == 'Junio' and (d >=1 and d <= 20)):
    print('Geminis')

elif (mes == 'Junio' and (d >=21 and d <= 30 )) or (mes == 'Julio' and (d >=1 and d <= 22)):
    print ('Cancer') 

elif (mes == 'Julio' and (d >=23 and d <= 31 )) or (mes == 'Agosto' and (d >=1 and d <= 22)):
    print  ('Leo') 

elif (mes == 'Agosto' and (d >=23 and d <= 31 )) or (mes == 'Septiembre' and (d >=1 and d <= 22)):
    print ('Virgo') 

elif (mes == 'Septiembre' and (d >=23 and d <= 30 )) or (mes == 'Octubre' and (d >=1 and d <= 22)):
    print  ('Libra')

elif (mes == 'Octubre' and (d >=23 and d <= 31 )) or (mes == 'Noviembre' and (d >=1 and d <= 21)):
        print ('Escorpío')

elif (mes == 'Noviembre' and (d >=22 and d <= 30 )) or (mes == 'Diciembre' and (d >=1 and d <= 21)):
    print ('Sagitario')

elif (mes == 'Diciembre' and (d >=22 and d <= 31 )) or (mes == 'Enero' and (d >=1 and d <= 19)):
    print ('Capricornio') 

elif (mes == 'Enero' and (d >=20 and d <= 31 )) or (mes == 'Febrero' and (d >=1 and d <= 18)):
    print  ('Acuario') 

elif (mes == 'Febrero' and (d >=19 and d <= 28 )) or (mes == 'Marzo' and (d >=1 and d <= 20)):
    print ('Pisis')