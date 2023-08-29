def palindromo(palabra):
  a=[]
  for i in range(len(palabra)):
    if  palabra[0+i]==palabra[len(palabra)-i-1]:
        a.append("contador")
  if len(a)==len(palabra):
    return True
  else:
    return False

           