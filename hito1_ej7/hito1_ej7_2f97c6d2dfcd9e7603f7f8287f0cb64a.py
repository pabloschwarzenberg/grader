day = int(input())
month = input()
astro_sign = str

if month == '12':
    astro_sign = 'Sagitario' if (day < 22) else 'capricornio'

elif month == '1':
    astro_sign = 'capricornio' if (day < 20) else 'Acuario'

elif month == '2':
    astro_sign = 'Acuario' if (day < 19) else 'Piscis'

elif month == '3':
    astro_sign = 'Piscis' if (day < 21) else 'Aries'

elif month == '4':
    astro_sign = 'Aries' if (day < 20) else 'tauro'

elif month == '5':
    astro_sign = 'tauro' if (day < 21) else 'geminis'

elif month == '6':
    astro_sign = 'geminis' if (day < 21) else 'cancer'

elif month == '7':
    astro_sign = 'cancer' if (day < 23) else 'leo'

elif month == '8':
    astro_sign = 'leo' if (day < 23) else 'virgo'

elif month == '9':
    astro_sign = 'Virgo' if (day < 23) else 'libra'

elif month == '10':
    astro_sign = 'Libra' if (day < 23) else 'Escorpio'

elif month == '11':
    astro_sign = 'Escorpio' if (day < 22) else 'Sagitario'

print(astro_sign)
