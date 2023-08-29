def buscarTodas(a,b):
  posiciones = []
  nuevo = ''
  for var in range(len(a)):
    if a[var] == b:
      posiciones.append(str(var))
  for var in posiciones:
    nuevo += var + ' '
  nuevo = nuevo[:-1]
  return nuevo

if __name__ == "__main__":
  a = input('Ingrese texto: ')
  b = input('Ingrese letra: ')
  buscarTodas(a,b)