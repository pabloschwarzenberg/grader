def buscarTodas(a,b):
  pos=[]
  largo=len(a)
  for n in range(0,largo):
    if a[n]==b:
      pos.append(str(n))
  pos=" ".join(pos)
  return pos

if __name__ == "__main__":
    a=input("")
    b=input("")
    print(buscarTodas(a,b))
           