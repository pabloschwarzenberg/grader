def buscarTodas(cadena, letra):
   Lista = []
   i=0
   while i <len(cadena): 
      if cadena[i] == letra:
        Lista = Lista +[i] 
      i= i+1 
   return " ".join(map(str,Lista)) 

if __name__ == "__main__":    
 cadena = input("Ingresa una frase: ")
 letra = input("Ingresa una letra: ")
 respuesta = buscarTodas(cadena, letra)
 print (respuesta)





           