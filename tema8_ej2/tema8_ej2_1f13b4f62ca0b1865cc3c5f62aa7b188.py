
def buscarTodas(a,b):
    
    cant = a.count(b)
    pos = - len(b)
    posiciones = []
    for c in range(cant): 
        pos = a.find(b, pos+len(b))
        if pos != -1: 
            posiciones.append(str(pos))

    posiciones = ' '.join(posiciones)
    return posiciones

if __name__ == "__main__":
    print(
        buscarTodas('tres tristes tigres', 't')
    )
        
