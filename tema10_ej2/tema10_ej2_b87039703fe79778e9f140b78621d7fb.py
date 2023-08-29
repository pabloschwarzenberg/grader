#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    count=0
    for i in range(len(palabra1)):
        for j in range(len(palabra2)):
            if palabra1[i]==palabra2[j]:
                print("True")
                count+=1
                print(count)
            else:
                count=count
                print("False")
                print(count)

    for i in range(len(palabra1)):
        if palabra1.count(palabra1[i])==1:
            count=count
        else:
            count=count-1
            print(count)
    for i in range(len(palabra2)):
        if palabra2.count(palabra2[i])==1:
            count=count
        else:
            count=count-0.5
            print(count)
    if len(palabra1)>len(palabra2):
        contador=len(palabra1)
    elif len(palabra1)<len(palabra2):
        contador=len(palabra2)
    elif len(palabra1)==len(palabra2):
        if palabra1==palabra2:
            contador=len(palabra1)-2
        else:
            contador=len(palabra1)
    contadorf=contador-count
    if contadorf>1:
          a="+1"
          return a
            
    elif contadorf==1:
          if len(palabra1)!=len(palabra2):
              a="IB"
              return a
            
          elif len(palabra1)==len(palabra2):
              a="1S"
              return a
                
    elif contadorf==0:
        a="0D"  
        return a
          
if __name__=="__main__":
    palabra1=str(input("ingrese una palabra:"))
    palabra2=str(input("ingrese una palabra:"))
    levenshtein(palabra1,palabra2)
    print(levenshtein(palabra1,palabra2))
