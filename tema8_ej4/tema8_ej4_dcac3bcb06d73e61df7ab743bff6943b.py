def rot13(palabra):
  pal=list(palabra)
  alf1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
  alf2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
  cesar=[]
  lar=len(pal)
  i=0
  j=0
  while i<lar:
    if pal[i]==alf1[j]:
        cesar.append(alf2[j])
        i+=1
        j=0
    elif pal[i]==alf2[j]:
        cesar.append(alf1[j])
        i+=1
        j=0
    else:
        j+=1
  cesar="".join(cesar)
  return cesar
  pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print(a)
           