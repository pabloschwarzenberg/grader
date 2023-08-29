#Zodiaco
print('Averigue su zodiaco')
dia = int(input('Dia de nacimiento: '))
mes = int(input('Mes de nacimiento: '))

zodiac_dict = {
    'Aries':{'start_month':3,
            'start_day':21,
            'end_month':4, 
            'end_day':19},
    'Taurus':{'start_month':4,
            'start_day':20,
            'end_month':5, 
            'end_day':20},
    'Gemini':{'start_month':5,
            'start_day':21,
            'end_month':6, 
            'end_day':20},
    'Cancer':{'start_month':6,
            'start_day':21,
            'end_month':7, 
            'end_day':22},
    'Leo':{'start_month':7,
            'start_day':23,
            'end_month':8, 
            'end_day':22},
    'Virgo':{'start_month':8,
            'start_day':23,
            'end_month':9, 
            'end_day':22},
    'Libra':{'start_month':9,
            'start_day':23,
            'end_month':10, 
            'end_day':22},
    'Scorpio':{'start_month':10,
            'start_day':23,
            'end_month':11, 
            'end_day':21},
    'Sagittarius':{'start_month':11,
            'start_day':22,
            'end_month':12, 
            'end_day':21},
    'Capricorn':{'start_month':12,
            'start_day':22,
            'end_month':1, 
            'end_day':19},
    'Aquarius':{'start_month':1,
            'start_day':20,
            'end_month':2, 
            'end_day':19},
    'Pisces':{'start_month':2,
            'start_day':20,
            'end_month':3, 
            'end_day':20},
}

for i,x in zodiac_dict.items():
    if mes == x['start_month']: #and dia > x['start_day']:
        if dia >= x['start_day']:
            print('Tu Zodiaco es: ',i)
    if mes == x['end_month']:
        if dia <= x['end_day']:
            print('Tu Zodiaco es: ',i)