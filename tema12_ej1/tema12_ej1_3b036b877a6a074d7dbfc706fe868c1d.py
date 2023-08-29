lb=[]
def falt(solucion):
  solucion +="0"
  return solucion
  
def scalt(solucion,n):
  if (len(solucion))<n:
    solucion += "1"
    return solucion
  else:
    return
    
def aceptar(candidato,n):
  global lb
  if len(candidato)== n and (candidato not in lb):
    lb.append(candidato)
    return True
def rechazar(candidato,n):
 if (candidato in lb):
   return True
def backtracking(candidato,n):
  global lb
  if aceptar(candidato,n):
    return
  if rechazar(candidato,n):
    return
  solucion=falt(candidato)
  for i in range(2):
   backtracking(solucion,n)
   solucion=scalt(candidato,n)
  return
backtracking("",10)
for n in lb:
  print(n)
  