V = eval(input())
Var_1 = V/10000000
tmp = V % 10000000
Var_2 = tmp / 1000000
tmp = tmp % 1000000
Var_3 = tmp / 100000
tmp = tmp % 100000
Var_4 = tmp / 10000
tmp = tmp %10000
Var_5 = tmp / 1000
tmp = tmp % 1000
Var_6 = tmp / 100
tmp = tmp % 100
Var_7 = tmp / 10
tmp = tmp % 10
Var_8 = tmp / 1
tmp = tmp % 1

#print("%i" % Var_1)
#print("%i" % Var_2)
#print("%i" % Var_3)
#print("%i" % Var_4)
#print("%i" % Var_5)
#print("%i" % Var_6)
#print("%i" % Var_7)
#print("%i" % Var_8)

Var_1 = int("%i" % Var_1)
Var_2 = int("%i" % Var_2)
Var_3 = int("%i" % Var_3)
Var_4 = int("%i" % Var_4)
Var_5 = int("%i" % Var_5)
Var_6 = int("%i" % Var_6)
Var_7 = int("%i" % Var_7)
Var_8 = int("%i" % Var_8)

Var_1 = Var_1 * 3
Var_2 = Var_2 * 2
Var_3 = Var_3 * 7
Var_4 = Var_4 * 6
Var_5 = Var_5 * 5
Var_6 = Var_6 * 4
Var_7 = Var_7 * 3
Var_8 = Var_8 * 2

Var_9 = Var_1 + Var_2 + Var_3 + Var_4  + Var_5 + Var_6 + Var_7 + Var_8
#print(Var_9)

Var_10 = Var_9 // 11
#print(Var_10)

Var_11 = Var_9 - (11 * Var_10)
#print(Var_11)

Var_12 = 11 - Var_11
#print(Var_12)

if Var_12 == 11:
  print("dv=0")
elif Var_12 == 10 :
  print("dv=k")
else:
  print("dv=",Var_12)