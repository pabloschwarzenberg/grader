sec=input()
genoma="ACTG"

def validar(sec):
  i=0
  while i<len(genoma):
    if sec.find(genoma[i])!=-1 and genoma[i]=="A" or genoma[i]=="C" or genoma[i]=="T" or genoma[i]=="G":
      return True
    else:
      return False
    i+=1
validar=validar(sec)
if validar==True:
  print("secuencua correcta")
else:
  print("secuencia incorrecta")
   