Var_1 = eval(input())
Var_3 = []
while Var_1 != 0 :
  Var_2 = Var_1 / 2
  if Var_2 == int(Var_2):
    #print("0",end="")
    Var_3.append("0")
  else:
    #print("1",end="")
    Var_3.append("1")
  Var_1 = int(Var_2)

Var_3 = "".join(reversed(Var_3))
Var_4 = eval(Var_3)
print("resultado =",Var_4)