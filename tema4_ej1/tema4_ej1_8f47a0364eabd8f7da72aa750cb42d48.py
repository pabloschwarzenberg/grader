import random

def ocultar_letras(palabra,cantidad):
      palabra=list(palabra)
      cantidad=int(cantidad)
      veces=0
      while veces<=cantidad:
        veces+=1
        i=random.randint(0,cantidad)
        palabra[i]="_"
        
        if veces>cantidad:
            palabralista=str(palabra)
            break
        
      return palabralista 

def revisar_letra(palabra_secreta,palabra,letra):
      p=""
      palabra_secreta=str(palabra_secreta)
      a=len(palabra)
      cantidad=random.randint(0,a-1)
      palabra=str(ocultar_letras(palabra,cantidad))
      a=len(palabra)
      letra=str(letra)
      if letra in palabra_secreta:
        for i in range(0,a):
          contador=[]
          if palabra_secreta[i]==letra:
            contador.append(i)
        
      for j in contador:
          palabra=list(palabra)
          palabra[j] = letra
          p.join(palabra)
      
      return palabra
    

if __name__ == "__main__":
    palabra=input()
    a=len(palabra)
    a=int(a)
    cantidad= random.randint(0,a-1)
    print(ocultar_letras(palabra, cantidad))
    intentos=0
    while intentos<7:
      letra=input()
      print(revisar_letra(palabra,ocultar_letras(palabra, cantidad),letra))
      
      if intentos<=7:
       break