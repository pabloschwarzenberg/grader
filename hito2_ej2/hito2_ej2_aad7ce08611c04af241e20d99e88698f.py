ADN=input()
ADN.upper
#ADN=list(ADN)
validar=ADN.count("A")+ADN.count("C")+ADN.count("T")+ADN.count("G")
if validar==len(ADN):
  print("secuencia correcta")
else:
   print("secuencia incorrecta")