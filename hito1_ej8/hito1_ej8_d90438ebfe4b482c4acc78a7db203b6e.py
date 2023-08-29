V = eval(input())
M = V/1000
tmp = V % 1000
C = tmp / 100
tmp = tmp % 100
D = tmp / 10
U = tmp % 10
if ("M%i" % M) != "M0" :
  print("%i" % M,"M",end="+")
if ("C%i" % C) != "C0" :
  print("%i" % C,"C",end="+")
if ("D%i" % D) != "D0" :
  print("%i" % D,"D",end="+")
if ("U%i" % U) != "U0" :
  print("%i" % U,"U")