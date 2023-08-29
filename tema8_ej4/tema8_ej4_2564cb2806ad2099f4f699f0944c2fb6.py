def rot13(palabra):
  palabra2=""
  abc=[]
  a="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
  for i in a:
    abc.append(i)
  for j in palabra:
    encontrado=False
    for k in range(0,len(a)):
      if j==a[k] and encontrado==False:
        j=a[k+13]
        encontrado=True
        palabra2+=j
  return palabra2
 

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
    pass
           