#Zodiaco
mes=input('mes: ')
dia=int(input('dia: '))
if mes=='marzo' and 21<=dia<31 or mes=='abril' and dia<20:
  r='Aries'
elif mes=='abril' and 20<=dia<31 or mes=='mayo' and dia<21:
  r='Tauro'
elif mes=='mayo' and 21<=dia<31 or mes=='junio' and dia<21:
  r='Géminis'
elif mes=='junio' and 21<=dia<31 or mes=='julio' and dia<23:
  r='Cáncer'
elif mes=='julio' and 23<=dia<31 or mes=='agosto' and dia<23:
  r='Leo'
elif mes=='agosto' and 23<=dia<31 or mes=='septiembre' and dia<23:
  r='Virgo'
elif mes=='septiembre' and 23<=dia<31 or mes=='octubre' and dia<23:
  r='Libra'
elif mes=='octubre' and 23<=dia<31 or mes=='noviembre' and dia<22:
  r='Escorpio'
elif mes=='noviembre' and 23<=dia<31 or mes=='diciembre' and dia<22:
  r='Sagitario'
elif mes=='diciembre' and 22<=dia<31 or mes=='enero' and dia<20:
  r='Capricornio'
elif mes=='enero' and 20<=dia<31 or mes=='febrero' and dia<19:
  r='Acuario'
elif mes=='febrero' and 29<=dia<31 or mes=='marzo' and dia<21:
  r='Piscis'
print(r)      