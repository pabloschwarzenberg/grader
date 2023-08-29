def buscarTodas(a,b):
      x=0
      p=''
      for i in a:
          if i==b:
              p=p+str(x)+' '  
          x+=1
      print(p)
      return (p.strip())
buscarTodas('tres tristes tigres','t')