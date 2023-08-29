def sopaletras(matrix,palabras):
            
    tuples=[]
    s=""
    for i in range(len(matrix)):#INDICE DE LA FILA
        for j in range(len(matrix[0])):
            s=""
            for i1 in range(len(matrix)):#COLUMNA VERIFIER ABAJO DIRECTION
                if 0<=i+i1<len(matrix):                    
                    s+=matrix[i+i1][j]
                    if s in palabras:                        
                        tuples.append((s,[i,j],"abajo"))
            s=""
            for i1 in range(len(matrix)):#COLUMNA VERIFIER ARRIBA DIRECTION
                if 0<=i-i1<len(matrix):
                    s+=matrix[i-i1][j]
                    if s in palabras:
                        tuples.append((s,[i,j],"abajo"))
            s=""
            for i1 in range(len(matrix[0])):#FILA VERIFIER DERECHA DIRECTION
                if 0<=j+i1<len(matrix[0]):
                    s+=matrix[i][j+i1]
                    if s in palabras:
                        tuples.append((s,[i,j],"derecha"))
            s=""
            for i1 in range(len(matrix[0])):#FILA VERIFIER IZQUIERDA DIRECTION
                if 0<=j-i1<len(matrix[0]):
                    s+=matrix[i][j-i1]
                    if s in palabras:
                        tuples.append((s,[i,j],"derecha"))
            s=""
            for i1 in range(max(len(matrix),len(matrix[0]))):#DIAGONAL \ ABAJO
                if 0<=i+i1<len(matrix) and 0<=j+i1<len(matrix[0]):
                    s+=matrix[i+i1][j+i1]
                    if s in palabras:
                        tuples.append((s,[i,j],"diagonal"))
            s=""
            for i1 in range(max(len(matrix),len(matrix[0]))):#DIAGONAL \ ARRIBA
                if 0<=i-i1<len(matrix) and 0<=j-i1<len(matrix[0]):
                    s+=matrix[i-i1][j-i1]
                    if s in palabras:
                        tuples.append((s,[i,j],"diagonal"))
            s=""
            for i1 in range(max(len(matrix),len(matrix[0]))):#DIAGONAL / ARRIBA
                if 0<=i+i1<len(matrix) and 0<=j-i1<len(matrix[0]):
                    s+=matrix[i+i1][j-i1]
                    if s in palabras:
                        tuples.append((s,[i,j],"diagonal"))
            s=""
            for i1 in range(max(len(matrix),len(matrix[0]))):#DIAGONAL / ARRIBA
                if 0<=i-i1<len(matrix) and 0<=j+i1<len(matrix[0]):
                    s+=matrix[i-i1][j+i1]
                    if s in palabras:
                        tuples.append((s,[i,j],"diagonal"))
            s=""
    archivo.close()
    return tuples
        

def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    l=[]
    for i in archivo:
        l1=[]
        for j in i:
            if j!=" ":
                j1=j.lower()
                l1.append(j1)
        l.append(l1[:-1])
    matrix=l        
    tuples=[]
    s=""
    for i in range(len(matrix)):#INDICE DE LA FILA
        for j in range(len(matrix[0])):
            s=""
            for i1 in range(len(matrix)):#COLUMNA VERIFIER ABAJO DIRECTION
                if 0<=i+i1<len(matrix):                    
                    s+=matrix[i][j]
                    if s in palabras:                        
                        tuples.append((s,[i,j],"abajo"))
            s=""
            for i1 in range(len(matrix)):#COLUMNA VERIFIER ARRIBA DIRECTION
                if 0<=i-i1<len(matrix):
                    s+=matrix[i-i1][j]
                    if s in palabras:
                        tuples.append((s,[i,j],"abajo"))
            s=""
            for i1 in range(len(matrix[0])):#FILA VERIFIER DERECHA DIRECTION
                if 0<=j+i1<len(matrix[0]):
                    s+=matrix[i][j]
                    if s in palabras:
                        tuples.append((s,[i,j],"derecha"))
            s=""
            for i1 in range(len(matrix[0])):#FILA VERIFIER IZQUIERDA DIRECTION
                if 0<=j-i1<len(matrix[0]):
                    s+=matrix[i][j-i1]
                    if s in palabras:
                        tuples.append((s,[i,j],"derecha"))
            s=""
            for i1 in range(max(len(matrix),len(matrix[0]))):#DIAGONAL \ ABAJO
                if 0<=i+i1<(len(matrix)-1) and 0<=j+i1<(len(matrix[0])-1):
                    s+=matrix[i+i1][j+i1]
                    if s in palabras:
                        tuples.append((s,[i,j],"diagonal"))
            s=""
            for i1 in range(max(len(matrix),len(matrix[0]))):#DIAGONAL \ ARRIBA
                if 0<=i-i1<len(matrix) and 0<=j-i1<len(matrix[0]):
                    s+=matrix[i-i1][j-i1]
                    if s in palabras:
                        tuples.append((s,[i,j],"diagonal"))
            s=""
            for i1 in range(max(len(matrix),len(matrix[0]))):#DIAGONAL / ARRIBA
                if 0<=i+i1<len(matrix) and 0<=j-i1<len(matrix[0]):
                    s+=matrix[i+i1][j-i1]
                    if s in palabras:
                        tuples.append((s,[i,j],"diagonal"))
            s=""
            for i1 in range(max(len(matrix),len(matrix[0]))):#DIAGONAL / ARRIBA
                if 0<=i-i1<len(matrix) and 0<=j+i1<len(matrix[0]):
                    s+=matrix[i-i1][j+i1]
                    if s in palabras:
                        tuples.append((s,[i,j],"diagonal"))
            s=""
    
    return tuples       

if __name__ == "__main__":
   sopaletras(input())


           