#Aprobación de créditos
ip = int(input('Ingreso (en pesos): '))
adn = int(input('Año de nacimiento: '))
ndh = int(input('Numero de hijos: '))
apb = int(input('Años de pertencia al banco: '))
soc = str(input('Estado civil("S": soltero / "C": casado): '))
uor = str(input('Vive en campo o ciudad ("U": urbano / "R": rural): '))

S = 1
C = 2
U = 3
R = 4

if (apb >= 10 and ndh >= 2) or\
   (soc == C and ndh > 3 and 1965 <= adn <= 1975) or\
   (ip < 2500000 and soc == S and uor == C) or\
   (ip < 3500000 and apb > 5) or\
   (uor == R and soc == C and ndh < 2):
    print('APROBADO')    
else:
    print('RECHAZADO')