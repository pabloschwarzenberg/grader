def levenshtein(str1, str2):
  str1=str(str1).lower
  str2=str(str2).lower
  if len(str1)>len(str2):
    i=0
    err=0
    while i<len(str2):
      if str2[i] not in str1:
        err+=1
      i+=1
    if err>1:
      return'+1'
  if len(str2)>len(str1):
    i=0
    err=0
    while i<len(str2):
      if str1[i] not in str2:
        err+=1
      i+=1
    if err>1:
      return'+1'
  if len(str2)==len(str1):
    i=0
    err=0
    while i<len(str2):
      if str1[i] not in str2:
        err+=1
      i+=1
    if err>1:
      return'+1'
    elif err==1:
      return'1S'
  if len(str1)>len(str2):
    if (len(str1)-len(str2))==1:
      return 'IB'
  if len(str2)>len(str1):
    if (len(str2)-len(str1))==1:
      return 'IB'
  if str1==str2:
    return '0D'