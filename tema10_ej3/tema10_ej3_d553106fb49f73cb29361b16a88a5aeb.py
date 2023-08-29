def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo,'r')    
    M=[]
    palabras = [ x.lower() for x in palabras ]
    lineas = archivo.readlines() 
    for linea in lineas:
        l1 = linea.split('\n')[0]
        l2 = l1.split(' ')
        M.append( [x.lower() for x in l2] )    
    archivo.close()
    candidatos = []
    partida = []
    for j in range(len(M)):
        for i in range(len(M[0])):
            
            n = buscar_linea(M,[i,j],'N')
            s = buscar_linea(M,[i,j],'S')
            
            e = buscar_linea(M,[i,j],'E')
            o = buscar_linea(M,[i,j],'O')
            
            ne = buscar_linea(M,[i,j],'NE')
            no = buscar_linea(M,[i,j],'NO')
            se = buscar_linea(M,[i,j],'SE')
            so = buscar_linea(M,[i,j],'SO')
                        
            partida.append([i,j])
            candidatos.append( [n,s,e,o,ne,no,se,so] )
    
    resultado = [] 
#    print(candidatos)
    for p in palabras:
        
        for i in range(len(candidatos)):     
            for j in range(len(candidatos[i])):
                if p == candidatos[i][j]:
                    if j in [0,1]:
                        direccion = 'derecha'
                    elif j in [2,3]:
                        direccion = 'abajo'
                    elif j in [4,5,6,7]:
                        direccion = 'diagonal'
                    resultado.append( (p, partida[i], direccion ) )
    
    return resultado



def buscar_linea(matriz, pos, direccion):
    
    i = pos[0]
    j = pos[1]
    
    if i<0 or j<0:
        return ''
    if i>=len(matriz) or j>=len(matriz[0]):
        return ''
    palabra = matriz[i][j]
    
    if direccion == 'N':
        palabra += buscar_linea(matriz, [i,j-1], direccion)
    elif direccion == 'S':
        palabra += buscar_linea(matriz, [i,j+1], direccion)
    elif direccion == 'E':
        palabra += buscar_linea(matriz, [i+1,j], direccion)
    elif direccion == 'O':
        palabra += buscar_linea(matriz, [i-1,j], direccion)
        
    elif direccion == 'NE':
        palabra += buscar_linea(matriz, [i+1,j-1], direccion)
    elif direccion == 'NO':
        palabra += buscar_linea(matriz, [i-1,j-1], direccion)
    elif direccion == 'SE':
        palabra += buscar_linea(matriz, [i+1,j+1], direccion)
    elif direccion == 'SO':
#        print(i,j, palabra)
        palabra += buscar_linea(matriz, [i+1,j-1], direccion)
        
    else:
        print('?')
        
    return palabra






if __name__ == '__main__':
    
    print( sopaletras ("sopa.txt", ["casa"]) )
    print( sopaletras ("sopa.txt", ["aro"]) )
