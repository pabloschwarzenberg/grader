def buscarTodas(a,b):
  r = ""
  for i in a:
    ni = a.index(i)
    if i is b:
      r += str(ni)+" "
      a = a.replace(a[ni], "N", 1)
  
  r = r[:-1]
  return r

if __name__ == "__main__":
    print(buscarTodas("tres tristes tigres", "t"))
           