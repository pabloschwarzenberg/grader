def decodificar(mensaje):
  mensaje = mensaje.split(",")
  letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","z"]
  lista = []
  i = 0
  while i < len(mensaje):
    letra = int(mensaje[i], 2)
    lista.append(letras[letra-97])
    i = i + 1
  mensaje = "".join(lista)
  return mensaje
   


         