texto = []
def jerigonzo(texto):
  texto = input('ingresar texto: ')
  texto = texto.upper()
  cifra = {
   'A': 'APA',
   'E': 'EPE',
   'I': 'IPI',
   'O': 'OPO',
   'U': 'UPU'
    }

  texto2 = []
  for letra in texto:
    texto2.append(cifra.get(letra, letra))
  texto2 = "".join(texto2)
  texto2 = texto2.capitalize()

  return texto2

print(jerigonzo(texto))