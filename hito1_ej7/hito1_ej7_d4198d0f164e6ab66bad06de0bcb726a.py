#Zodiaco
from datetime import date

def getZodiacSigns(m,d):
    zodiacSigns = ['Capricornio','Acuario','Picis','Aries',
                    'Tauro','Geminis', 'Cancer', 'Leo', 
                    'Virgo', 'Libra','Escorpion', 'Sagitario'
                ]
    return zodiacSigns[m-1] if d < 21 else zodiacSigns[m]

def reqNumber(reqText):
    while True:
        number = input(reqText)
        try:
            return int(number)
        except ValueError:
            print("Debes ingresar un número entero. \nInténtalo de unuevo \n")

day = reqNumber("Ingresa el día: ")
month = reqNumber("Ingresa el mes: ")
zodiacSign = getZodiacSigns(month,day)
print(zodiacSign)