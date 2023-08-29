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
  numero_de_palabras = 0
  largo_promedio = 0
  n_espacios = 0
  n_punct = 0
  palabra = ""
  frase_original = frase
  frase = frase.replace("\n", " ")
  for c in range(len(frase)):
    palabra += frase[c]
    if frase[c] == "." and frase[c+1] == "." and frase[c+2] == ".":
      numero_de_palabras += 1
      largo_promedio += len(palabra[:-1])
      n_punct += 3
      palabra = ""
      break
    elif frase[c] == " ":
      if not palabra == " ":
        numero_de_palabras += 1
      largo_promedio += len(palabra.strip())
      palabra = ""
  for c in frase_original:
    if c == " ":
      n_espacios += 1
  largo_promedio /= numero_de_palabras
  return numero_de_palabras, len(frase_original), largo_promedio, n_espacios, n_punct

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))