import random
def ocultar_letras(palabra,cantidad):
    listaCambiada=[]
    for i in palabra:
        listaCambiada.append(i)
    for numero in range(0,cantidad):
        indexAleatorio= random.randint(0,len(palabra)-1)
        listaCambiada[indexAleatorio]= "_"
        palabra="".join(listaCambiada)
        
    return palabra

listaRandom=["lepidoptero", "cocaina", "matias", "pirulin"]
indexRandom= random.randint(0,len(listaRandom)-1)
palabra= listaRandom[indexRandom]
palabra_secreta=palabra 
cantidad= random.randint(0,len(palabra)-1)

def revisar_letra(palabra_secreta,palabra,letra):
  if letra in palabra_secreta:
    
    palabra= palabra.replace("_",letra)
    return palabra

if __name__ == "__main__":
    pass
         