def levenshtein(palabra1,palabra2):
    palabra1 = list(palabra1)
    palabra2 = list(palabra2)
    contador = 0
    i = 0
    if len(palabra1) == len(palabra2):
      while i < len(palabra1):
        if palabra1[i] == palabra2[i]:
          i += 1
        else:
            i += 1
            contador += 1
      if contador == 0:
         return "0D"
      elif contador == 1:
         return "1S"
      else:
         return "+1"
    else:
        if abs(len(palabra1) - len(palabra2)) > 1:
            return "+1"
        else:
            while contador < 1 and i < len(max([palabra1, palabra2])):
                if palabra1[i] == palabra2[i]:
                    i += 1
                    continue
                else:
                    contador += 1
            if contador == 1:
                return "1B"
            else:
                return "+1"