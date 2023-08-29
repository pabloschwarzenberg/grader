def buscarTodas(a,b):
  result=[]
  for i in range(len(a)):
    if a[i]==b:
      result.append(str(i))
  return " ".join(result)

if __name__ == "__main__":
    a=input()
    b=input()
    print(buscarTodas(a,b))   