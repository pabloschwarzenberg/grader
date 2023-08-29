#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    resta=abs(len(palabra1)-len(palabra2))
    i=0
    suma=0
    j=0
    if len(palabra1)>len(palabra2):
        mayor=palabra1
        menor=palabra2
    else:
        mayor=palabra2
        menor=palabra1
    if resta==0:
        while i<len(mayor):
            letra1=palabra1[i]
            letra2=palabra2[i]
            if letra1==letra2:
                suma+=1
            i+=1
    if resta!=0:
         for i in mayor:
             while j<len(menor):
                 letra1=menor[j]
                 if i==letra1:
                     suma+=1
                 j+=1
    if suma==len(palabra1):
            return "0D"
    if resta==0 and suma!=len(palabra1):
            return "1S"
    if resta>=1 and suma>1:
            return "+1"
    if resta==1 and suma==1:
            return "IB"
    else:
        return "+1"
            
        
    
    

           