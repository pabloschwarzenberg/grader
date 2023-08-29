mitad1 = []#Letras de A - M en codigo ascii
mitad2 = [] #Letras de N - Z en codigo ascii
for i in range(97,110):
  mitad1.append(i)
for i in range(110,123):
  mitad2.append(i) 

def rot13(palabra):
  palabra_rot = "" 
  for i in palabra:
    #busca en que mitad está la letra según su codigó ascii
    if ord(i) in mitad1:
      #Se busca el indice de la letra
      indice = mitad1.index(ord(i))
      #se busca por indice en la otra mitad del alfbeto y se retorna el caracter del codigo ascii
      palabra_rot += chr(mitad2[indice])
    #se repite lo mismo pero cambiando roles.
    elif ord(i) in mitad2:
      indice = mitad2.index(ord(i))
      palabra_rot += chr(mitad1[indice])
  return(palabra_rot)
      

if __name__=="__main__":
    
    
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           