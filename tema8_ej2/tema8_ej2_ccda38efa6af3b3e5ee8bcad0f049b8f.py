def buscarTodas(a,b):
 string=''
 contador=0
 for c in a:
   if(c==b):
     if(string==''):
       str1=str(contador)
       string+=str1
       contador=contador+1
     else:
       string+=' '
       nstr=str(contador)
       string+=nstr
       contador=contador+1
   else:
     contador=contador+1
 return(string)
print(buscarTodas('tres tristes tigres','t'))

