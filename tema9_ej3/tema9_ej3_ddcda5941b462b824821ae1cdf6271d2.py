def esCambio(str1, str2):

  strAux = ''

  encontrada = False

  i = 0

  while i < len(str1) and not(encontrada):

    if str1[i] != str2[i]:

      encontrada = True

      strAux = strAux + str2[i + 1 : len(str2)]

    else:

      strAux = strAux + str2[i]

    i = i + 1

  return strAux == str1