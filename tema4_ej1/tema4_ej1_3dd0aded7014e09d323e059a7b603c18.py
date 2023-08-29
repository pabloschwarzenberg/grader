def ocultar_letras(palabra,cantidad):
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
  palabra=list(palabra)
  if palabra_secreto==letra:
    palabra=palabra_secreta
    return palabra
    
  for i in range(0,len(palabra)):
    if letra==palabra_secreta[i]:
      palabra.insert(i,letra)
      palabra.pop(i+1)
  palabra="".join(palabra)
  return palabra
pass

if __name__ == "__main__":
    pass
         