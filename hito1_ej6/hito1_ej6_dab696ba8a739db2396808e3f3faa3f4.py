a = eval(input("primer numero = "))
b = eval(input("segundo numero = "))
c = eval(input("tercer numero = "))
if a > b and a>=c :
  print (f"{c},{b},{a}")
if b > a and b >c :
  print (f"{a},{c},{b}")
if c > a and c >=b :
  print (f"{a},{b},{c}")