letras = "ACTG"
sec = input()
win = True 
for a in sec:
    if a.capitalize() not in sec:
        print("secuencia incorrecta")
        win = False
        break 
       
if win:
  print("secuencia correcta")
        