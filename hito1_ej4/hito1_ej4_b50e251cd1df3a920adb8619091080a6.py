#Conversión de Decimal a Binario
numero=int(input("ingrese numero "))
guarda=""
indice=0
binario=""
while(numero>0):
  parte=numero//2  #28//2 14
  resto=numero%2   #28%2   0
  guarda=guarda+str(resto)  #"0" 
#  print(parte,resto,guarda)
  numero=numero//2
indice=len(guarda)-1
while(indice >=0 ):
  #print(guarda[indice],end="")
  binario=binario+guarda[indice]
  indice=indice-1
print(eval(binario))