NT = int(input())
HLL = int(input())

if HLL >= 0 and HLL <= 7:
  print("CONTESTAR")

elif HLL < 14 and NT % 1000 == 909:
  print("CONTESTAR")

elif HLL >= 17 and HLL <= 19 and NT // 100000 == 877:
  print(" NO CONTESTAR")

else:
  print("NO CONTESTAR")