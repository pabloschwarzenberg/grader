import random
l=["hola","adios","salir","Sueño"]
palabra=random.choice(l)
cantidad=len(palabra)
def ocultar_letras(palabra,cantidad):
  b=random.randint(0,cantidad)
  p=palabra[0:b]+ "-" + palabra[b+1:]
  return p
palabra_secreta=" "
letra=" "
def revisar_letra(palabra_secreta,palabra,letra):
  if palabra == palabra_secreta:
    return("ganaste")
  
  else:
    return("perdiste")
  

if __name__ == "__main__":
  x=revisar_letra(palabra_secreta,palabra,letra)
  y=ocultar_letras(palabra,cantidad)
  print(y)
  palabra_secreta=input("Adivina la palabra: ")
  palabra_secreta=palabra_secreta.lower()
  letra=input("adivina la letra: ")
  letra=letra.lower()
  print(x)
  print(palabra_secreta)
 


  
