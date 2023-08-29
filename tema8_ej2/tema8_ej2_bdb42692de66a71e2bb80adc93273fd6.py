def buscarTodas(a,b):
 string=''
 acumular=0
 for correcto in a:
   if(correcto==b):
     if(string==''):
       str1=str(acumular)
       string+=str1
       acumular=acumular+1
     else:
       string+=' '
       nstr=str(acumular)
       string+=nstr
       acumular=acumular+1
   else:
     acumular=acumular+1
 return(string)
print(buscarTodas('tres tristes tigres','t'))