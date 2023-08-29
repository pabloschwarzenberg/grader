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
    
    frase = frase.lower()
    
    sig = [";",",","!","?","¡",":",".","¿"]
    
    let = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
      "n","o","p","q","r","s","t","u","v","w","x","y","z",
      "á","í","é","ó","ú"]
    
    x = 0
    
    w = 0
    
    y = 0
    
    z = 0
    
    v = 0
    
    for p in frase:
         
         if p in let and frase[v+1] not in let:
            
            x += 1
         
         if p in let:
           
           w += 1
         
         if p in sig:
         
           y += 1
         if p not in let and p not in sig:
             
             z +=1
         v += 1
    
    a = list(frase)
    
    b = len(a)
    
    c = 0 
    
    for q in a:
       
       if q==" ":
          
          c +=1
          
    largo_a = w/x
    
    return x,b,largo_a,c,y
if __name__ == "__main__":
    
    print(estadisticas_frase(hombre_imaginario))
         