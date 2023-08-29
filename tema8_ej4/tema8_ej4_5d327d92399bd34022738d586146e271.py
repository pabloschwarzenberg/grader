import string
def rot13(palabra):
  a=string.ascii_lowercase
  n=13
  txt=" "
  for i in palabra:
    s=a.find(i)+n
    m=s % len(a)
    txt=txt+str(a[m])
  return txt

if __name__=="__main__":
   palabra=input("Ingresa la palabra que quieras encriptar: ")
   palabra.lower()
   resultado=rot13(palabra)
   print("El resultado es: ",resultado)
           