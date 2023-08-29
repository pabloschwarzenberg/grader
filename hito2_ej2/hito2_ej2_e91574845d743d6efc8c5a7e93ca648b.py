l1=str(input("Ingrese la cadena: "))
caca=l1.upper()
while True:
  if len(l1)==0:
    print("secuencia correcta")
    break 
    
  if caca[0]=="A" or caca[0]=="T" or caca[0]=="C" or caca[0]=="G":
    caca=caca[1::]
  else:
    print("secuencia incorrecta")
    break
    
