def buscarTodas(a,b):
          m=[i for i,x in enumerate(a) if x==b]
          z=list(m)
          l=[]
          for i in z:
                    l.append(str(i))
          w=" ".join(l)
          return w
--------------------------------
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
            esp2+=1
    prom_largo = cac/pal
    return pal,new2,prom_largo,esp2,pun
    #return pal,cac,prom_largo,esp,pun

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
