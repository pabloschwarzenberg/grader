string=input()
numero=int(input())
largo=len(string)
if(largo%numero!=0):
  print("ninguna")
else:
  c=largo/numero
  if(c==2):
    x=string[:numero]
    y=string[numero:]
    print(x,y)
  elif(c==3):
    x=string[:numero]
    y=string[numero:(numero+numero)]
    z=string[(numero+numero):]
    print(x,y,z)
  elif(c==1):
    print(string)
    
  
  