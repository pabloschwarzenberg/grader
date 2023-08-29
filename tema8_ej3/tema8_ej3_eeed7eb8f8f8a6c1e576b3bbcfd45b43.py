hombre_imaginario = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""

def estadisticas_frase(frase):
   
    var_ListaPalabras = frase.split()
    var_NumPalabras = len(var_ListaPalabras)
    var_CantCaracteres = len(frase)
    var_CantEspacios = 0
    var_ListaPromedio = []
    var_Especiales = 0
    
    for indice in var_ListaPalabras:
        
        if indice == "imaginarios...":
            var_ListaPromedio.append(len(indice) - 3)
            
            for p in indice:
                
                if p == ".":
                    var_Especiales += 1
        
        else:
            var_ListaPromedio.append(len(indice))
    
    promedio_letras = sum(var_ListaPromedio) / var_NumPalabras
    
    print(promedio_letras)

    for indice in frase:
        
        if " " in indice:
            var_CantEspacios += 1
    
    mensaje = (var_NumPalabras, var_CantCaracteres, promedio_letras, var_CantEspacios, var_Especiales)
    
    return mensaje

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))