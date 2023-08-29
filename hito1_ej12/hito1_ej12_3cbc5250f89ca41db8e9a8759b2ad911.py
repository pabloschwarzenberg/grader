numMinimo = 1
numMaximo = 20

from random import *
nDigitos=int(input("Elige el número   :"))
if nDigitos>=1 and nDigitos<=20 :
  lSuperior="20"*nDigitos
  numeroIntentos="0"*(nDigitos-1)
  lInferior="1"+cCero
  nroAdivinar=str(randint(int(numMinimo), int(numMaximo) ) )
  print (nroAdivinar)
else :
  print ("Deben ser entre 1 y 20")
