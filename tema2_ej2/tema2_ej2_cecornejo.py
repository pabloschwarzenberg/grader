# completa el código de la función
def amigos(a,b):
  lista=[]
  lista_b=[]
  for i in range (1,a+1):
      if a//i == 0:
         lista=lista.append(i)
         largo=len(lista)
         contador=1
         while contador <= largo:
             suma_final=0
             suma_final+= lista[contador]    #con este codigo lo que busco es que cada divisor
                                             # de "a" quede guardado en una lista para luego sumarlos
  
  for i in range (1,b+1):           
       if b//i == 0:
         lista_b=lista_b.append(i)
         largo=len(lista)
         contador=1
         while contador <= largo:
             suma_final_b=0
             suma_final_b+= lista_b[contador]
             
        if suma_final== b or suma_final_b==1:
                 return True
        else:
          Return False
       
 