#Aprobación de créditos
import datetime
anyo_actual = datetime.date.today().year
ingresos = int(input('Ingresos (en pesos): '))
anyo_nacimiento = int(input('Introducir año de nacimiento: '))

numero_de_hijos =  int(input('Introducir numero de hijos: '))
anyos_de_permanencia_banco =int(input('Introducir numero de años de permanencia : '))
# Opciones S = soltero, C = casado33
estado_civil = input('Introducir estado civil (S=Soltero, C=Casado) : ').lower()
# Opciones U = Urbano, R = Rural
vivienda = input('Introducir ubicacion vivienda (U=Urbano, R=Rural) : ').lower()


edad_calculada = anyo_actual - anyo_nacimiento
print(edad_calculada)

# IF y ELIF's controlan las condiciones
if anyos_de_permanencia_banco>10 and numero_de_hijos>=2:
    print('APROBADO')
elif ((estado_civil =='c' and numero_de_hijos > 3) and (45 < edad_calculada <55)):
    print('APROBADO')
elif ((estado_civil =='s' and vivienda =='u') and (ingresos > 2500000)):
    print('APROBADO')
elif ((anyos_de_permanencia_banco>5) and (ingresos > 3500000)):
    print('APROBADO')
elif ((estado_civil =='c' and vivienda =='r') and (numero_de_hijos <2)):
    print('APROBADO')
else:
    print('RECHAZADO')      