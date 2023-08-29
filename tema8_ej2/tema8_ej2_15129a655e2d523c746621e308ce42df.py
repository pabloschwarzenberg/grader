def buscarTodas(frase,letra):

 largo=len(frase)
 i=0
 p="S"
 respuesta=str()

 posicion=str()
 while i<largo and i>=0 and posicion!="-1":
    
     posicion=str(frase.find(letra,i))

    
     if posicion!="-1":
        
         if p=="S":
            
             p="N"
             respuesta=respuesta+posicion
            
         else:
             respuesta=respuesta+" "+posicion
           
     else:
         break
    
     i=int(posicion)+1

 return respuesta