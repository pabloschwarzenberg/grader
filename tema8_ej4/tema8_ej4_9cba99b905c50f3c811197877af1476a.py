def rot13(palabra):
  palabra=list(palabra)
  letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  conjunto1=letras[0:13]
  conjunto2=letras[13:27]
  cesar=[]
  i=0
  while i<len(palabra):
    if conjunto1.count(palabra[i])==1:
      posicion=conjunto1.index(palabra[i])
      cesar.append(conjunto2[posicion])
    elif conjunto2.count(palabra[i])==1:
      posicion=conjunto2.index(palabra[i])
      cesar.append(conjunto1[posicion])
    i+=1
  cesar="".join(cesar)
  return cesar
           