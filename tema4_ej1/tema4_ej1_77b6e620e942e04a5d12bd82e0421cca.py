import random
def buscarTodas(a,b):
  arreglo = []
  asd = ""
  for i in range(0,len(a)):
    if(a[i] == b):
      arreglo.append(i)
  for j in range(0,len(arreglo)): 
    asd = asd +" "+str(arreglo[j])
  asd = asd[1::]
  return asd

def ocultar_letras(palabra,a):
    alr = {}
    niuPalabra = list(palabra)
    for i in range(0,len(niuPalabra)):
        al = random.randint(0,len(niuPalabra))
        while(al in alr):
            al = random.randint(0,len(niuPalabra))

        alr[al] = ""
    print(alr)
    for j in alr:
        
        niuPalabra[j] = "_"
    return niuPalabra
##
##seguir = True
##arreglo = []
##while(seguir):
##    msj = "Ingrese una palabra o 1 para finalizar el ingreso: "
##    opc = input(msj)
##
##    if(opc == "1"):
##        seguir = False
##
##    else:
##        arreglo.append(opc)
##
##d = random.randint(0,len(arreglo))
##palabra = arreglo[d]
##a = random.randint(1,len(palabra))
##
##ocultar_letras(palabra,a)

      