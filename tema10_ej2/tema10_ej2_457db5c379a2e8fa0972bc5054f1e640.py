#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    a=len(palabra1)>len(palabra2)
    if a==True:
        lista1=[]
        lista2=[]
        lista3=[]
        for i in palabra1:
            lista1.append(i)
        for i in palabra2:
            lista2.append(i)
        for i in range(len(lista2)):
            if lista2[i] in lista1:
                lista1.remove(lista2[i])
        print(lista1)               
                
        if len(lista1)>1:
            return '+1'
        elif len(lista1)==1:
            if len(palabra1)==len(palabra2):
                return '1S'
            else:
                return 'IB'
        elif len(lista1)==0:
            return '0D'
    else:
        lista1=[]
        lista2=[]
        for i in palabra2:
            lista2.append(i)
        for i in palabra1:
            lista1.append(i)
        for i in range(len(lista1)):
            if lista1[i] in lista2:
                lista2.remove(lista1[i])
                
        if len(lista2)>1:
            return '+1'
        elif len(lista2)==1:
            if len(palabra1)==len(palabra2):
                return '1S'
            else:
                return 'IB'
        elif len(lista2)==0:
            return '0D'
           