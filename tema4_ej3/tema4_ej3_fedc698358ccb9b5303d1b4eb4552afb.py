def jerigonzo(string):
  x=[]
  cont=0
  q=""
  for z in string:
    x.append(z)
  for i in x:
    if i == "a":
      x[cont]="apa"
    if i == "e":
      x[cont]="epe"
    if i == "i":
      x[cont]="ipi"
    if i == "o":
      x[cont]="opo"
    if i == "u":
      x[cont]="upu"
    cont+=1
  for m in x:
    q+=str(m)
  
  return q

if __name__ == "__main__":
    pass
         