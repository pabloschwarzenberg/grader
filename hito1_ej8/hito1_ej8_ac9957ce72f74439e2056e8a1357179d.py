#Number break down
num = input("Input any number of up to 4 digits: ")
numLength = len(num)
if(numLength == 1):
  print("{}U".format(num))
elif(numLength == 2):
  U = num[1]
  D = num[0]
  print("{}D + {}U".format(D,U))
elif(numLength == 3):
  U = num[2]
  D = num[1]
  C = num[0]
  print("{}C + {}D + {}U".format(C,D,U))
elif(numLength == 4):
  U = num[3]
  D = num[2]
  C = num[1]
  M = num[0]
  print("{}M + {}C + {}D + {}U".format(M,C,D,U))