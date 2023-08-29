string=input("Ingrese secuencia: ")
def validar_secuencias(string):
  str=string.upper()
  lista=list(str)
  
  while "A" in lista:
    lista.remove("A")
    
  while "C" in lista:
    lista.remove("C")

  while "T" in lista:
    lista.remove("T")
  
  while "G" in lista:
    lista.remove("G")

  if len(lista)!=0:
    print("La secuencia",string,"es incorrecta")
  else:
    print("La secuencia",string,"es correcta")
    
validar_secuencias(string)
