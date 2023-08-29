#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    
    (m, n) = (len(palabra1), len(palabra2))
 
    
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]
 
    for i in range(1, m + 1):
        T[i][0] = i                    
 
    for j in range(1, n + 1):
        T[0][j] = j                    
 
    
    for i in range(1, m + 1):
 
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:          
                cost = 0                        
            else:
                cost = 1                       
 
            T[i][j] = min(T[i - 1][j] + 1,     
                        T[i][j - 1] + 1,        
                        T[i - 1][j - 1] + cost) 
 
    return T[m][n]
 
 
if __name__ == '__main__':
 
    palabra1= 'kitten'
    palabra2 = 'sitting'
 
    print('The Levenshtein distance is', levenshtein(palabra1,palabra2))
           