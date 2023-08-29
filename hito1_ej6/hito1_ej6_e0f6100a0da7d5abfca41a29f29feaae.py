var=int(input("escribe un numero: "))
var2=int(input("escribe un numero: "))
var3=int(input("escribe un numero: "))

if var<=var2 and var2<=var3:
  print(var,",",var2,",",var3)
if var>=var2 and var2>=var3:
  print(var3,",",var2,",",var)
if var<=var2 and var2>var3:
  print(var,",", var3,",", var2)
if var>var3 and var2<var3:
  print(var,",", var3,",", var2)