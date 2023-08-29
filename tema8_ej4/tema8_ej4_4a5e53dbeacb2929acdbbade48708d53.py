string1="abcdefghijklm"
string2="nopqrstuvwxyz"
def rot13(palabra):
    a=palabra
    a=list(a)
    for u in range(0,len(a)):
      for g in string1:
          if (a[u]==g):
              a[u]=string2[string1.find(a[u])]
              break
      else:
        a[u]=string1[string2.find(a[u])]
              
    return("".join(a))

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           