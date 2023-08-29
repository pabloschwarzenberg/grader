#Zodiaco
x = int(input("Dime un dia: "))
y = int(input("Dime un mes: ")) - 1
zodiaco = [{(x < 20): 'capricornio', (x >= 20): 'acuario'},
           {(x < 19): 'acuario', (x >= 19): 'piscis'},
           {(x < 21): 'piscis', (x >= 21): 'aries'},
           {(x < 20): 'aries', (x >= 20): 'tauro'},
           {(x < 21): 'tauro', (x >= 21): 'geminis'},
           {(x < 21): 'geminis', (x >= 21): 'cancer'},
           {(x < 23): 'cancer', (x >= 23): 'leo'},
           {(x < 23): 'leo', (x >= 23): 'virgo'},
           {(x < 23): 'virgo', (x >= 23): 'libra'},
           {(x < 23): 'libra', (x >= 23): 'escorpio'},
           {(x < 22): 'escorpio', (x >= 22): 'sagitario'},
           {(x < 22): 'sagitario', (x >= 22): 'capricornio'}
           ]
print(zodiaco[y][True])      