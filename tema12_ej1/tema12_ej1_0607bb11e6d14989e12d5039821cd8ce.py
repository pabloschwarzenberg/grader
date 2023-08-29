
def binarios(n,candidato=""):
  if len(candidato)==int(n):
    print(candidato)
  else:
    for p in ["0","1"]:
      candidato_aux=candidato+p
      binarios(n,candidato_aux)  
binarios(input())
