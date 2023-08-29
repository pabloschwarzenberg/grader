def rot13(palabra):
  a=list(palabra)
  alfabeto1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
  alfabeto2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
  x=[]
  largo=len(a)
  i=0
  j=0
  while i<largo:
    if a[i]==alfabeto1[j]:
        x.append(alfabeto2[j])
        i+=1
        j=0
    elif a[i]==alfabeto2[j]:
        x.append(alfabeto1[j])
        i+=1
        j=0
    else:
        j+=1
  x="".join(x)
  return x
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print(a)