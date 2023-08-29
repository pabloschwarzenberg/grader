__author__ = 'Domingo'
#La funcion debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if palabra1==palabra2:
        return '0D'
    else:
        if len(palabra1)==len(palabra2):
            contador=0
            for i in range(len(palabra1)):
                if palabra1[i]==palabra2[i]:
                    contador+=1
            if contador==len(palabra2)-1:
                return '1S'
            else:
                return '+1'
        else:
            lista_p1=[]
            lista_p2=[]
            for i in palabra1:
                lista_p1.append(i)
            for i in palabra2:
                lista_p2.append(i)
            if (len(palabra1)==len(palabra2)+1):
                for i in palabra1:
                    indice=palabra2.find(i)
                    if indice != -1:
                        lista_p2.pop(indice)
                        lista_p2.insert(indice,'*')
                numero_asteriscos=0
                for i in lista_p2:
                    if i=='*':
                        numero_asteriscos+=1
                if len(lista_p2)==numero_asteriscos:
                    return 'IB'
                else:
                    return '+1'

            elif (len(palabra1)+1==len(palabra2)):
                for i in palabra2:
                    indice=palabra1.find(i)
                    if indice != -1:
                        lista_p1.pop(indice)
                        lista_p1.insert(indice,'*')
                numero_asteriscos=0
                for i in lista_p1:
                    if i=='*':
                        numero_asteriscos+=1
                if len(lista_p1)==numero_asteriscos:
                    return 'IB'
            else:
                return '+1'
