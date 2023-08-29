cadena = input ("ingrese cadena: ")

cadena = cadena.replace('a','x')

cadena = cadena.replace('t','a')

cadena = cadena.replace('x','t')

cadena = cadena.replace('c','x')

cadena = cadena.replace('g','c')

cadena = cadena.replace('x','g')

if not cadena in "actg":
   print('secuencia incorrecta')
else:
    print(cadena)