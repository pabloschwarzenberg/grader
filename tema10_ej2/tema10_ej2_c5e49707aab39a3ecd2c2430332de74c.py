def levenshtein(str1, str2):

  if str1 == str2:

    return '0D'

  elif len(str1) == len(str2):

    varSubs = esSubstitucion(str1, str2)

    if varSubs:

      return '1S'

    else:

      return '+1'

  elif (len(str1)-len(str2) == -1):

    if esCambio(str1, str2):

      return 'IB'

    else:

      return '+1'

  elif (len(str1)-len(str2) == 1):

    if esCambio(str2, str1):

      return 'IB'

    else:

      return '+1'

  else:

    return '+1'





#print(lev('melon', 'melon'))
      return '+1'

  elif (len(str1)-len(str2) == -1):

    if esCambio(str1, str2):

      return 'IB'

    else:

      return '+1'

  elif (len(str1)-len(str2) == 1):

    if esCambio(str2, str1):

      return 'IB'

    else:

      return '+1'

  else:

    return '+1'





#print(lev('melon', 'melon'))           