#Contestador de celular
n=int(input())
h=int(input())
nu=n-((n//1000)*1000)
np=n//100000
if h>=0 and h<=7:
  print("CONTESTAR")
elif h>7 and h<=14:
  if nu==909:
    print("CONTESTAR")
  elif nu!=909:
    print("NO CONTESTAR")
elif h>14 and h<17:
  print("NO CONTESTAR")
elif h>=17 and h<=19:
  if np==877:
    print("NO CONTESTAR")
  elif np!=877:
    print("CONTESTAR")
elif h>19:
  print("NO CONTESTAR")