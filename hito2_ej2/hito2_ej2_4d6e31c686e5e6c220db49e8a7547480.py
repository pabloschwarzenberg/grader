string = str(input())
genoma = "ACTG"
i=0
cont = 0
while i < len(string):
     string = string.upper()
     let = string[i]
     if genoma.find(let) == -1:
         cont+=1
     else:
         cont+=0
     i+=1
        
if cont == 0:
      print("secuencia correcta")
else:
      print("secuencia incorrecta")
    
