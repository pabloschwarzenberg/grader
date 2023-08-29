#Contestador de celular
num = int(input("Input phone number: "))
time = eval(input("Phone call time: "))
if (time >= 0 and time <= 7):
  print("CONTESTAR")
elif((time <= 14) and ((num % 1000)==909)):
  print("CONTESTAR")
elif(time >= 17 and time <= 19):
  if((num // 100000 == 877)):
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
elif(time >= 19 and time <= 23):
  print("NO CONTESTAR")
else:
  print("NO CONTESTAR")