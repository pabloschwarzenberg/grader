import random



palabras=["Tropezar","Votar","Palacio","Individual","Largo","Alas","Empinado","Espiar","Pinza","Pelear"]
palabra=palabras
def ocultar_letras(palabra,cantidad):
  
  palabra=random.choice(palabra)
  palabra=palabra.lower()
  palabralist=list(palabra)
  while len(palabralist)<cantidad:
    palabra=random.choice(palabra)
    palabra=list(palabra)
  palabra=palabralist
  while cantidad>0:
    a=palabra.index(random.choice(palabra))

    if palabra[a]!="_":
      palabra[a]="_"
      cantidad=cantidad-1
  return palabra

def revisar_letra(palabra_secreta,palabra,letra):
  ocultar_letras(palabra,cantidad):



  
  return palabra



while True:


  cantidad=int(input("cuántas letras quieres ocultar? "))
  print(ocultar_letras(palabra,cantidad))
  palabra=palabras 
