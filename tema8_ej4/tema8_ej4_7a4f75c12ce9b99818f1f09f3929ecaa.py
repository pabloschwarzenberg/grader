def rot13(palabra):
  a_13=list("abcdefghijklm")
  b_13=list("nopqrstuvwxyz")
  rot13=[]
  for i in range(len(palabra)):
    if palabra[i] in a_13:
      for j in range(13):
        if palabra[i]==a_13[j]:
          rot13.append(b_13[j])
    elif palabra[i] in b_13:
      for j in range(13):
        if palabra[i]==b_13[j]:
          rot13.append(a_13[j])
  rot13="".join(rot13)
  return rot13