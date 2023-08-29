string = ''
def buscarTodas(a,b):
  global string
  for i in a:
    if i == b:
      c = a.find(i)
      string = string + str(c)
  return string

if __name__ == "__main__":
  abc = str(input("Ingrese su palabra "))
  bca = str(input("Ingrese el string que desea encontrar "))
  print(buscarTodas(abc,bca))

