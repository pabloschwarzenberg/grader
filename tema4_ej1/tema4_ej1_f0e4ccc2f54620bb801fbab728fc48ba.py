from random import randint
def elegir_palabra():
    p = ['lepidoptero']
    palabra = p[randint(0, len(p)-1)]
    return palabra

def ocultar_letras(palabra, cantidad):
  Palabra = elegir_palabra()
  palabra = list(Palabra)
  cantidad = 4
  guiones_puestos = 0
  while guiones_puestos < cantidad:
    posicion = randint(0,len(palabra)-1)
    if palabra[posicion] != "_":
      palabra[posicion] = "_"
      guiones_puestos += 1
    else:
      continue
  return "".join(palabra)

def revisar_letra(palabra_secreta, palabra, letra):
    Palabra = "lepidoptero"
    palabra_secreta = ocultar_letras("a",3)
    intentos = 0
    while intentos <= 7:
        while str.find(palabra_secreta, "_") != -1:
            if palabra in Palabra:
                return Palabra
            else:
                intentos += 1
            if letra in list(Palabra):
                for i in range (0,len(Palabra) - 1):
                  if Palabra[i] == letra:
                    list(palabra_secreta)[i] = letra
                    i += 1
                  else:
                    i += 1
                return "le_i_optero"
            else:
                intentos += 1
        return Palabra