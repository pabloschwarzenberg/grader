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

 largo=len(hombre_imaginario) 
 cant_pal=0
 espacios=0
 num=0
 l_pal=0
 cant_cp=0
 i=0
 letra_ant=str()
 fin="no"
 while i<largo:
 
     letra=hombre_imaginario[i]

     if (letra== " " or letra=="\n") and letra_ant!="\n":
         cant_pal=cant_pal+1
         if letra==" ":
             espacios=espacios+1
         num=num+l_pal
         l_pal=0
         palabra=str()
     else:
         if letra!="." and letra!="\n":
             l_pal=l_pal+1
         else:
              if letra=="." and letra_ant=="." and fin=="no":
                  num=num+l_pal
                  fin="si"              
                         
     if letra==".":
         cant_cp=cant_cp+1

     i=i+1
     letra_ant=letra

 promedio=num/cant_pal

 return(cant_pal,largo,promedio,espacios,cant_cp)

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))