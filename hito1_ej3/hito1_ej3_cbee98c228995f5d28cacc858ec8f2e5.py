#Aprobación de créditos
ing=int(input('Ingrese sus ingresos'))
nac=int(input('Ingrese su año de nacimiento'))
nh=int(input('Ingrese su cantidad de hijos'))
ab=int(input('Ingrese la cantidad de años que lleva en el banco'))
ec=input('Ingrese su estado civil "S":soltero , "C":casado')
lv=input('Ingrese su vivienda "U": urbano , "R":rural')
if (ab>10 and nh>=2) or (ec=='C' and nh>3 and (2020-nac)>45 and (2020-nac)<55) or (ing>2500000 and ec=='S' and lv=='U')\
        or (ing>3500000 and ab>5) or (ec=='C' and lv=='R' and nh<2):
                print('APROBADO')
else:
        print('RECHAZADO')