def ADN(string):
    i=0
    a=0
    lista="AaCcGgTt"
    L=list(lista)
    while i<len(string):
       if string[i] in L:
         i+=1
         a+=1
       else:
         i+=1
    if a==len(string):
      print("secuencia correcta")
    else:
      print("secuencia incorrecta")
 
string=input()
ADN(string)
    
       