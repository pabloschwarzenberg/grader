def levenshtein(palabra1,palabra2):

  a = palabra1 
  b = palabra2 
  sem = 0 
 
  if len(a) > len(b): a, b = b, a 
 
  ref = b 
  for letra in a: 
      if letra in b: 
          sem += 1 
          b = b.replace(letra, "", 1) 
 
  return "'%s' y '%s' difieren en: %i" %(a, ref, len(ref) - sem) 
               

if __name__=="__main__":
    pass
           