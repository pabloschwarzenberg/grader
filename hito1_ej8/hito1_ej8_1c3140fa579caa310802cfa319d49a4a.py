#Descomponer un número
x=[]
y=int(input('Ingrese un numero de hasta 4 digitos:'))
x.append(y)

if len(str(y)) == 4:
  print(str(x[0])[0]+'M', end='+')
  print(str(x[0])[1]+ 'C',end='+')
  print(str(x[0])[2]+'D',end='+')
  print(str(x[0])[3]+ 'U')

elif len(str(y)) == 3:
  print(str(x[0])[0]+ 'C',end='+')
  print(str(x[0])[1]+ 'D',end='+')
  print(str(x[0])[2]+ 'U')
    
elif len(str(y)) == 2:
  print(str(x[0])[0]+ 'D',end='+')
  print(str(x[0])[1]+ 'U')
    
elif len(str(y)) == 1:
  print(str(x[0])[0]+ 'U')