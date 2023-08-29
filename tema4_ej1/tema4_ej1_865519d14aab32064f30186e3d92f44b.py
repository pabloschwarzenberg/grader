def revisar_letra(palabra_secreta,palabra,letra):

  x = list(palabra_secreta)

  palabra = list(palabra)

  if letra in x:

    y = palabra_secreta.find("-")

    palabra[y] = letra

  palabra = "".join(palabra)

  print(palabra)

  return palabra
