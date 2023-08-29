def jerigonzo(string):
    i=0
    vocales=["a","e","i","o","u"]
    nueva=[]
    while i<len(string):
      nueva.append(string[i])
      if string[i] in vocales:
        nueva.append("p")
        nueva.append(string[i])
      i+=1
    nueva="".join(nueva)	
    return nueva