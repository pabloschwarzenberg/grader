def buscarTodas(a,b):
  i=0
  string=""
  for j in a:
    i = i + 1
    if j == b:
      string = string + str(i-1) + " "
      string = str(string)
  return string.rstrip()    
    

if __name__ == "__main__":
  a = input("Ingrese una frase")
  b = input("ingrese un elemento")
  print(buscarTodas(a,b))
    
           