def rot13(palabra):
  abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  cifradocesar = ''
  desplazamiento = 13
  for i in palabra.lower():
      if i in abecedario:
          if abecedario.index(i) < 13:
              cifradocesar += abecedario[abecedario.index(i) + 13]
          else:
              cifradocesar += abecedario[abecedario.index(i) - 13]
  
  return(cifradocesar)           