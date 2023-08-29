S=input("")
i=0
while i<len(S):
      if S[i]=="A" or S[i]=="T" or S[i]=="G" or S[i]=="C":
        if i==len(S)-1:
            print("Secuencia correcta")
        i=i+1
      else:
          print("Secuencia incorrecta")
          break
      