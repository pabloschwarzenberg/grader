#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

def levenshtein(palabra1,palabra2):
    x=len(palabra1)
    y=len(palabra2)
    response=''
    distancia=0
    a=list(palabra1)
    b=list(palabra2)
    if palabra1==palabra2:
        response='0D'

###################################################
    elif (x-y ==1) or (x-y== -1):
            if a>b:
                for i in range(len(b)):
                    if a[i]!=b[i]:
                        distancia+=1
                for k in range(len(b)):
                    if a[k]!=b[k]:
                        distancia-=1        
                k-=1
                i+=1

            elif b>a:
                for i in range(len(a)):
                    if a[i]!=b[i]:
                        distancia+=1
                for k in range(len(a)):
                    if a[k]!=b[k]:
                        distancia-=1        
                k-=1        
                i+=1
            if distancia <=1:
                response='IB'
            elif distancia>1:
                response='+1'
###################################################
                
    elif (x-y>1) or (x-y)<-1:
        response='+1'
    elif (x-y==0) or (x-y)==0:
            if a>b:
                for i in range(len(b)):
                    if a[i]!=b[i]:
                        distancia+=1
                i+=1

            elif b>a:
                for i in range(len(a)):
                    if a[i]!=b[i]:
                        distancia+=1        
                i+=1

            if distancia <=1:
                response='1S'
            elif distancia>1:
                response='+1'
    return response
if __name__=="__main__":
   palabra1=str(input("Diga la primera palabra:"))
   palabra2=str(input("Diga la segunda palabra:"))
   print(levenshtein(palabra1,palabra2))

           