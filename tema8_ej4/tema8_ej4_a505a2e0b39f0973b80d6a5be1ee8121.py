def rot13(palabra):
  p_13=list("abcdefghijklm")
  s_13=list("nopqrstuvwxyz")
  rot13=[]
  for i in range(len(palabra)):
    if palabra[i] in p_13:
      for j in range(13):
        if palabra[i]==p_13[j]:
          rot13.append(s_13[j])
    elif palabra[i] in s_13:
      for j in range(13):
        if palabra[i]==s_13[j]:
          rot13.append(p_13[j])
  rot13="".join(rot13)
  return rot13