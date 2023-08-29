def genoma (genoma1,genoma2,genoma3,genoma4):
  if (genoma1=="a")or(genoma1=="A"):
    if (genoma2=="t")or(genoma2=="T"):
      if(genoma3=="c")or(genoma3=="C"):
        if (genoma2=="g")or(genoma2=="G"):
          resultado=genoma1+genoma2+genoma3+genoma4    
    else:
      resultado=genoma2+genoma1+genoma4+genoma3
      
  elif (genoma1=="c")or(genoma1=="C"):
    if (genoma2=="g")or(genoma2=="G"):
      if (genoma3=="a")or(genoma3=="A"):
        if (genoma4=="t")or(genoma4=="T"):
          resultado=genoma1+genoma2+genoma3+genoma4
    else:
      resultado=genoma2+genoma1+genoma4+genoma3
      
  return resultado

genoma1=input()
genoma2=input()
genoma3=input()
genoma4=input()
respuesta=genoma(genoma1,genoma2,genoma3,genoma4)