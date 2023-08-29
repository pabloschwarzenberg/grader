import random
import os

max_fallos = 7

palabras = ["mariposa", "lepidoptero", "insecto"]
palabra = random.choice(palabras)

def ocultar_letras(palabra,cantidad):
  secreta = "_"*cantidad
  return secreta
    
palabra_secreta = ocultar_letras
print(ocultar_letras(palabra, random.randint(1, len(palabra))))
#print(secreta)
    
def revisar_letra(palabra_secreta,palabra,letra):
    revisar_letra=("e,i,o,p,t,r,o")
    for (revisar_letra):
        return false
    if (ocultar_letra):
        return true
      
    if (palabra_secreta):
        return palabra_secreta
      

if __name__ == "__main__":
    pass
         