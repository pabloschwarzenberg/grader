def buscarTodas(a,b):
  i=0
  string=""
  for _ in a:
    i= i+1
    if _ == b:
      string = string + str(i-1) + ' '
      string =str(string)

  return string.rstrip()

if __name__ == "__main__":
  a=input('Frase: ')
  b=input('Elemento: ')
  print (buscarTodas(a,b)) 