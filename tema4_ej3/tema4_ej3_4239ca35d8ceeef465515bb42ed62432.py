def jerigonzo(string):
  lista=[]
  suma=""
  for a in string:
    lista.append(a)
  for n in lista:
    if n in vocales:
      suma+=n+"p"+n
    else:
      suma+=n



  return suma
vocales=["a","e","i","o","u"]
if __name__ == "__main__":
  string=input("ingrese su palabra:")
  
  
  print(jerigonzo(string))
