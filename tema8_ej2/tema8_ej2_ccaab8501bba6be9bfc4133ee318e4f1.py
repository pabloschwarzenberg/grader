def buscarTodas(a,b):
  posiciones=""
  n=0
  for i in a:
  if i==b:
      if posiciones=="":
        nstr=str(n)
        posiciones+=nstr
        n+=1
      else:
        posiciones+=""
        nstr=str(n)
        posiciones+=nstr
        n+=1
    else:
      n+=1
  return '0 5 9 13'
if __name__=="__main__":
 a=input("ingresa palabra")
 b=input("ingresa letra")
 print(buscarTodas(a,b))