day = int(input("Input birthday: "))
month = input("Input month of birth (e.g. march, july etc): ")
meses = {
  "1": "january",
  "2": "february",
  "3": "march",
  "4": "april",
  "5": "may",
  "6": "june",
  "7": "july",
  "8": "august",
  "9": "september",
  "10": "october",
  "11": "november",
  "12": "december",
}
month = meses[month]

if month == 'december':
	astro_sign = 'sagitario' if (day < 22) else 'capricornio'
elif month == 'enero':
	astro_sign = 'capricornio' if (day < 20) else 'acuario'
elif month == 'february':
	astro_sign = 'acuario' if (day < 19) else 'piscis'
elif month == 'march':
	astro_sign = 'piscis' if (day < 21) else 'aries'
elif month == 'april':
	astro_sign = 'aries' if (day < 20) else 'tauro'
elif month == 'may':
	astro_sign = 'tauro' if (day < 21) else 'geminis'
elif month == 'june':
	astro_sign = 'geminis' if (day < 21) else 'cancer'
elif month == 'july':
	astro_sign = 'cancer' if (day < 23) else 'leo'
elif month == 'august':
	astro_sign = 'leo' if (day < 23) else 'virgo'
elif month == 'september':
	astro_sign = 'virgo' if (day < 23) else 'libra'
elif month == 'october':
	astro_sign = 'libra' if (day < 23) else 'escorpio'
elif month == 'november':
	astro_sign = 'escorpio' if (day < 22) else 'sagitario'
print(astro_sign)