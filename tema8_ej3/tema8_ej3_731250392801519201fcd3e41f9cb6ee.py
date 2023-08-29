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

def estadisticas(string):
    t=",."
    spaces=0
    for i in string:
        if i ==" ":
            spaces+=1
    
    string2=string.replace("\n"," ")
    string3=string2.replace(" ","")
    
    l2=string2.split(" ")
    l3=[]
    p=0
    for i in string3:
        if i=="," or i==".":
            p+=1
    
    
    for j in l2:
        if j!=" " and j!=" " and not(j in t):
            l3.append(j.replace(".",""))
    s=0#numero de palabras
    for i in l3:
        s+=1
    s1=0
    for i in l3:
        s2=0
        for j in i:
            s2+=1
        s1+=s2
    promedio=s1/s
    print s
    print len(string3)
    print promedio
    print spaces
    print p
    
            
            
            
    
    
    
    

    

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         