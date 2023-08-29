entrance = str(input('ingrese secuencia: '))
def genoma(entrance):
  
  ADN = 'A,C,T,G'
  if entrance.upper() == ADN:
    return print('secuencia correcta')
  else:
    return print('secuencia incorrecta')

genoma(entrance)