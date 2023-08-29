#Zodiaco
dia = int(input('Dia de nacimiento: '))
mes = int(input('Mes de nacimiento: '))

signos = [('Aries',21,21), ('Tauro',21,21), ('Geminis',21,21), ('Cancer',21,23), ('Leo',23,23)]
signos +=  [('Virgo',23,23), ('Libra',23,23), ('Scorpio',23,22), ('Sagitario',23,22), ('Capricornio',22,20), ('Acuario',20,19), ('Piscis',19,21)]
signo = ''
m = 3
i = 0

while signo == '':

    if m > 12:
        m = 1

    sig = m+1 if m < 12 else 1 
    if (dia > signos[i][1] and mes == m) or (dia <= signos[i][2] and mes == sig):
        signo = signos[i][0]
    
    m += 1
    i += 1 

print(signo)     