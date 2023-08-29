def buscarTodas(a, b):
    def encontrarIndices(a, b):
        indices = []
        index = -1
        
        while True:
            index = a.find(b, index + 1)
            if index == -1:
                break
            indices.append(str(index))
        
        return indices
    
    def generarSecuencia(indices):
        return ' '.join(indices)
    
    indices = encontrarIndices(a, b)
    secuencia = generarSecuencia(indices)
    
    return secuencia
