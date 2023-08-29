#Aprobación de créditos
a = 0
ingres_os = int(input())
anac = int(input())
n_hijo= int(input())
vej_ban= int(input())
relac = str(input()) #quizas definelo como func para que tome argumentos "S", "C"
vive = str(input()) # lo mismo de relac, pero con "U", "R"
if vej_ban > 10 and n_hijo >=2:
  print("APROBADO")
if relac == "C" and n_hijo > 3 and anac <= 1972 and anac >= 1962:
  print("APROBADO")
if ingres_os > 2500000 and relac == "S" and vive == "U":
  print("APROBADO")
if ingres_os > 3500000 and vej_banc > 5:
  print("APROBADO")
if n_hijo < 2 and relac == "C" and vive == "R":
  print("APROBADO")
