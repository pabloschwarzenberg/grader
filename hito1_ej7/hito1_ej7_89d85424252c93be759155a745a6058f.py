day = int(input("Ingresa el día: "))
month = int(input("Ingresa el mes: "))
astro_sign = ''
if month == 12:
    astro_sign = 'sagitario' if (day < 22) else 'capricornio'
elif month == 1:
    astro_sign = 'capricornio' if (day < 20) else 'aquario'
elif month == 2:
    astro_sign = 'aquario' if (day < 19) else 'picis'
elif month == 3:
    astro_sign = 'picis' if (day < 21) else 'aries'
elif month == 4:
    astro_sign = 'aries' if (day < 20) else 'tauro'
elif month == 5:
    astro_sign = 'tauro' if (day < 21) else 'geminis'
elif month == 6:
    astro_sign = 'geminis' if (day < 21) else 'cancer'
elif month == 7:
    astro_sign = 'cancer' if (day < 23) else 'leo'
elif month == 8:
    astro_sign = 'leo' if (day < 23) else 'virgo'
elif month == 9:
    astro_sign = 'virgo' if (day < 23) else 'libra'
elif month == 10:
    astro_sign = 'libra' if (day < 23) else 'escorpio'
elif month == 11:
    astro_sign = 'escorpio' if (day < 22) else 'sagitario'

print(astro_sign)