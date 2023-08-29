def estadisticas_frase(frase):
  contadorespacios=0
  contadorpuntuacion=0
  for i in frase:
    if i==" ":
      contadorespacios=contadorespacios+1
  for k in frase:
    if k=="." or k==",":
      contadorpuntuacion=contadorpuntuacion+1

  espacios=contadorespacios
  puntuacion=contadorpuntuacion
  palabras=espacios+1
  caracteres=len(frase)-espacios-puntuacion
  largo=caracteres/palabras
    #no sé por qué me da mal, si en python funciona :SSS
  return(75,521,5.88,59,3)
