def buscarTodas(a,b):
  string=""
  contador_2=0
  contador_3=contador_2
  while contador_2<=len(a)-1:
    if a[contador_2]==b:
        contador_3=contador_2
        contador_3=str(contador_3)
        string=string+" "+contador_3
        contador_2=contador_2+1
    else:
        contador_2=contador_2+1
  string=string.strip()
  return string

if __name__ == "__main__":
    pass
           