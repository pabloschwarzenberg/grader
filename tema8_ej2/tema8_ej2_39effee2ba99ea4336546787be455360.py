def buscarTodas(a,b):
  num=0
  veces=a.count(b)
  string3=""
  exe=""
  
  
  for i in range(veces): 
    string3+=str(a[num:].find(b)+num)
    string3+=" "
    num+=(a[num:].find(b)+1)
    exe=(string3[0:-1])
    
  return (exe)




if __name__ == "__main__":
    buscarTodas("tres tristes tigres","t")
           