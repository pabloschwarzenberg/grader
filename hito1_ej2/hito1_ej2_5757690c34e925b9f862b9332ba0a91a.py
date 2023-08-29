n=input("ingrese numero telefonico: ")
h=int(input("ingrese hora de llamada: "))

num=n[-3]+n[-2]+n[-1]
num2=n[0]+n[1]+n[2]

if h>=0 and h<7:
  print("CONTESTAR")
elif h<14:
  if num=="909":
    print("CONTESTAR")
  elif num!="909":
    print("NO CONTESTAR")
elif h>=17 and h<19:
  if num2=="877":
    print("NO CONTESTAR")
  elif num2!="877":
    print("CONTESTAR")
elif h>19:
  print("NO CONTESTAR")