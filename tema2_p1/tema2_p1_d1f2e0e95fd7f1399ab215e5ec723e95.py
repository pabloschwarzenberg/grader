def es_primo(A):
  DVS=1
  CDD=0
  while DVS<=A:
    if A%DVS==0:
      CDD=CDD+1
    DVS=DVS+1
  if CDD==2:
    return True
  else:
    return False
           