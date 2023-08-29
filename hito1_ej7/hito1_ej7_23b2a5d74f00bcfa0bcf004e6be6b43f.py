#Zodiaco

day = int(input("Input birthday: "))
month = int(input("Input month of birth (e.g. march, july etc): "))

# of a specified zodiac
if month == 12:
    astro_sign = 'Sagittario' if (day < 22) else 'capricornio'
      
elif month == 1:
    astro_sign = 'Capricornio' if (day < 20) else 'aquarius'
      
elif month == 2:
    astro_sign = 'acuario' if (day < 19) else 'piscis'
      
elif month == 3:
    astro_sign = 'piscis' if (day < 21) else 'aries'
      
elif month == 4:
    astro_sign = 'aries' if (day < 20) else 'taurus'
      
elif month == 5:
    astro_sign = 'tauro' if (day < 21) else 'geminis'
      
elif month == 6:
    astro_sign = 'geminis' if (day < 21) else 'cancer'
      
elif month == 7:
    astro_sign = 'Cancer' if (day < 23) else 'leo'
      
elif month == 8:
    astro_sign = 'Leo' if (day < 23) else 'virgo'
      
elif month == 9:
    astro_sign = 'Virgo' if (day < 23) else 'libra'
      
elif month == 10:
    astro_sign = 'Libra' if (day < 23) else 'scorpio'
      
elif month == 11:
    astro_sign = 'scorpio' if (day < 22) else 'sagittario'
      
print("Tu zodiaco es: ", astro_sign)