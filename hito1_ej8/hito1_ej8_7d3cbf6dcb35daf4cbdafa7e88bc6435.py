#Descomponer un número
numero = int(input('Ingrese Número: ')) 
if numero >= 1000:
  a = str(numero)[:1]
  b = str(numero)[1:2]
  c = str(numero)[2:3]
  d = str(numero)[3:]

  print(a,'M + ', b,'C + ', c,'D + ',d,'U' )

elif 99 < numero < 1000:    
  a = str(numero)[:1]
  b = str(numero)[1:2]
  c = str(numero)[2:]

  print(a,'C + ', b,'D + ',c,'U' )

elif 9 < numero < 99:
    a = str(numero)[:1]
    b = str(numero)[1:]

    print(a,'D + ',b,'U' )

elif 0 <= numero < 9:
    a = str(numero)[:]
    print(a,'U' )