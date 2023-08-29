def divisores(f):
    divisores=[]
    w=f
    for f in range(1,f):
        if(w/f==w//f):
            divisores.append(f)
    return(divisores)
def numero_perfecto(a):
  y=0
  for g in divisores(a):
      y=y+g      
  if(y==a):
      return(True)
  else:
      return(False)

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           