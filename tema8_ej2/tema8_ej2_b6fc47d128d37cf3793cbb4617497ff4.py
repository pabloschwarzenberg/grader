def buscarTodas(a,b):
  lista=""
  for i in range(len(a)):
    if a[i]==b:
        pico=str(i)
        lista+=pico
        lista+=" "
  returnar=lista[0:len(lista)-1]  
  return returnar

if __name__ == "__main__":
    pass
           
           
           
           
           