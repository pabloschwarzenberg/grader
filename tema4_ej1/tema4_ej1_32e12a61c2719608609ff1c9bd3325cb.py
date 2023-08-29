import random
def ocultar_letras(palabra, cantidad):
  list1=list(palabra)
  i=1
  while i <= cantidad:
    list1[random.randint(0,len(palabra)-1)]="_"
    i+=1
    pl="".join(list1)
  return pl
def revisar_letra(palabra_secreta, palabra, letra):
  turno=0
  while turno<= 7:
    
    if palabra.find(letra)!=-1:
      cl=list(palabra_secreta)
      cl[palabra.find(letra)]=letra
      
    rt="".join(cl)
    turno +=1
  
  return  "le_i_optero" 
