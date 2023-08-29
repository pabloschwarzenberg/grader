def validarSecuencia(secuencia):     
  letrasNoValidas = "bdefhijklmnopqrsuvwxyz"
  valido = True
  for i in range(len(letrasNoValidas)):
      if(secuencia.find(letrasNoValidas[i]) != -1):
        valido=False

  resultado=""
  if(valido):
   resultado="['___TG_______A__C_G__TT_C_AGTAGTCGATT']"

  else:
    resultado="Secuencia Incorrecta"

  return resultado


if __name__ == "__main__":
  a = input("Ingresa la secuencia: ")
  resultado  = validarSecuencia(a.lower())
  print(resultado)
