import random
def ocultar_letras(palabra,cantidad):
   contador=0
   listaindices=list()
   while contador<cantidad:
     contador=contador+1
     indice=random.randint(0,len(palabra)-1)
     while indice in listaindices:
      indice=random.randint(0,len(palabra)-1)
     listaindices.append(indice)
     nueva_palabra=str()
     for i in range(len(palabra)):
      if i==indice:
       nueva_palabra=nueva_palabra + "_"
      else:
       nueva_palabra=nueva_palabra + palabra[i]
     palabra=nueva_palabra
   return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
   nuevapalabra=str()
   for i in range(len(palabra_secreta)):
    if palabra_secreta[i]==letra:
     nuevapalabra=nuevapalabra + letra
    else:
     nuevapalabra=nuevapalabra + palabra[i]
   return nuevapalabra


print ("hola")
