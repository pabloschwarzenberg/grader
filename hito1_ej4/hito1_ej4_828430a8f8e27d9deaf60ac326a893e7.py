dml = int(input('que numero desea pasar a binario: '))
bi = ''
while dml // 2 != 0:
  bi = str(dml % 2) + bi
  dml = dml // 2
  x=str(dml) + bi
print( 'resultado=', x)

