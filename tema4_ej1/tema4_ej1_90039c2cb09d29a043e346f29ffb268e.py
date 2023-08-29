import random

def ocultar_letras(palabra,cantidad):
  i=0
  largo=len(palabra)
  ocultar=random.randint(1,largo)
  while i<=cantidad:
    palabra.replace(palabra[ocultar],"_")
    ocultar=random.randint(1,largo)
    i=i+1
  return palabra

def revisar_letra(palabra_secreta,palabra,letra):
  for i in range(0,len(palabra)):
    if palabra_secreta.count[letra]!=0:
      primer_=palabra.find["_"]
      palbra[primer_]="letra"

if __name__ == "__main__":
    pass
         