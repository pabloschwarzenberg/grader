genoma=input()
genoma.upper()
gen=list(genoma)
for nucl in gen:
    if nucl=="A" or nucl=="G" or nucl=="T" or nucl=="C":
       g=True
    else:
       g=False
if g==True:
   print("secuencia correcta")
if g==False:
   print("secuencia incorrecta")