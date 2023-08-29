import random
palabras = ["lepidoptero","casa","avioneta","escuela","universidad"]
palabra = random.choice(palabras)

def ocultar_letras(palabra,cantidad):
  palabra_oculta = palabra
  for i in range(cantidad):
    print(i)
    letra = random.choice(palabra_oculta)
    palabra_oculta = palabra_oculta.replace(letra,"_")
  print(palabra_oculta)
  return (palabra_oculta)

def revisar_letra(palabra,palabra_oculta,letra):
  if letra in palabra:
    lst =list()
    for i in range(len(palabra)):
      if palabra[i] == letra:
        lst.append(i)
    for i in lst:
      palabra_oculta = palabra_oculta[:i] + letra + palabra_oculta[i+1:]
    print(palabra_oculta)
    return (palabra_oculta)

if __name__ == "__main__":
  cantidad = int(input("Ingrese cantidad:\n"))
  palabra_oculta = ocultar_letras(palabra,cantidad)
  letra = input("Ingrese una letra:\n")
  revisar_letra(palabra,palabra_oculta,letra)