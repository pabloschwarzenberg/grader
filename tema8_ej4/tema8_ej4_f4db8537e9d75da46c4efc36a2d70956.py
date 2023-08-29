def rot13(palabra):
  a=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
  n=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
  p=list(palabra)
  i=0
  j=0
  while j<len(p):
    if a[i]==p[j]:
      p[j]=n[i]
      i=0
      j=j+1
      continue
    elif n[i]==p[j]:
      p[j]=a[i]
      i=0
      j=j+1
      continue
    i=i+1
  palabra="".join(p)
  return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           