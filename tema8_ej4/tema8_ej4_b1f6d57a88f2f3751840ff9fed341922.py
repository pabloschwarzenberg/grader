def rot13(pala):
  pal=list(pala)
  alf=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
  alff=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
  empty=[]
  lar=len(pal)
  i=0
  j=0
  while i<lar:
    if pal[i]==alf[j]:
        empty.append(alff[j])
        i+=1
        j=0
    elif pal[i]==alff[j]:
        empty.append(alf[j])
        i+=1
        j=0
    else:
        j+=1
  empty="".join(empty)
  return empty
  pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print(a)