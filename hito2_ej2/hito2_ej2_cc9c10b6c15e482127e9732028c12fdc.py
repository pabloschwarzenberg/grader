def validarSecuencia(secuencia):
  letrasNoValidas = "bdefhijklmnopqrsuvwxyz"
  valido = True
  for i in range(len(letrasNoValidas)):
      if(secuencia.find(letrasNoValidas[i]) != -1):
        valido=False

  resultado=""
  if(valido):
   resultado="Secuencia Correcta"
  else:
    resultado="Secuencia Incorrecta"

  return resultado


if __name__ == "__main__":
  a = input("Ingresa la secuencia: ")
  ñ=input('ingresa la secuencia: ')
  c=input('ingresa la secuencia: ')  
  resultado  = validarSecuencia(a.lower())
  print(resultado)


if __name__ == "__main__":
  a = input("Ingresa la secuencia: ")
  resultado  = validarSecuencia(a.lower())
  print(resultado)
      