#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if palabra1 == palabra2:
       return "OD"
    else:
        letras_distintas = 0
        if(len(palabra1) == len(palabra2)):
            largo = len(palabra1)
            lista = []
            for i in palabra1:
                lista.append(i)
            for j in palabra2:
                lista.append(j)
        
            letras_distintas = 0
            k = 0
            while k<largo:
                if lista[k]==lista[k+largo]:
                     letras_distintas = letras_distintas
                     k = k + 1
                else:
                     letras_distintas = letras_distintas + 1
                     k = k + 1
            if letras_distintas == 1:
                return "1S"
            if letras_distintas>1:
                return "+1"
            
                
                
        if(len(palabra1) != len(palabra2)):
              distancia = abs(len(palabra1)-len(palabra2))
              distancia_total = distancia
              lista_final = []
              if distancia_total > 1:
                 return "+1"
              else:
                  if len(palabra1)>len(palabra2):
                       lista1 = []
                       lista2 = []
                       for i in palabra1:
                           lista1.append(i)
                       for j in palabra2:
                           lista2.append(j)
          
                       lista1.remove(lista1[len(palabra1)-1])
                       letras_distintas = 0
                       for i in lista1:
                           lista_final.append(i)
                       for j in lista2:
                           lista_final.append(j)
                        
                       k = 0
                       letras_distintas = 0
                       largo1 = len(lista1)
                       while k<largo1:
                           if lista_final[k]==lista_final[k+largo1]:
                                letras_distintas = letras_distintas
                                distancia_total = distancia_total
                                k = k + 1
                           else:
                                letras_distintas = letras_distintas + 1
                                distancia_total = distancia_total + letras_distintas
                                k = k + 1
                       if distancia_total == 1:
                           return "1B"
                       else:
                           return "+1"
                    
                  else:
                       lista1 = []
                       lista2 = []
                       for i in palabra1:
                           lista1.append(i)
                       for j in palabra2:
                           lista2.append(j)
          
                       lista2.remove(lista2[len(palabra1)-1])
                       letras_distintas = 0
                       for i in lista1:
                           lista_final.append(i)
                       for j in lista2:
                           lista_final.append(j)
                        
                       k = 0
                       letras_distintas = 0
                       largo2 = len(lista2)
                       while k<largo2:
                           if lista_final[k]==lista_final[k+largo2]:
                                letras_distintas = letras_distintas
                                distancia_total = distancia_total
                                k = k + 1
                           else:
                                letras_distintas = letras_distintas + 1
                                distancia_total = distancia_total + letras_distintas
                                k = k + 1
                       
                       if distancia_total == 1:
                          return "1B"
                       else:
                          return "+1"
    

if __name__=="__main__":
    palabra1 = input("Ingrese primera palabra:")
    palabra2 = input("Ingrese segunda palabra:")
    print(levenshtein(palabra1,palabra2))

           