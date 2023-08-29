def jerigonzo(string):
  vocales="aeiouAEIOU"
  traduccion=""
  for jeri in string:
    traduccion+= jeri
    if jeri in vocales:
      traduccion+="p"+jeri
  return traduccion

         