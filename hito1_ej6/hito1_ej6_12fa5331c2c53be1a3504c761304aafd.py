A=float(input("Número A: "))
B=float(input("Número B: "))
C=float(input("Número C: "))
if (A <= B <= C):
  print(int(A),",",int(B),",",int(C))

else:
  if (B <= A <= C):
    print(int(B),",",int(A),",",int(C))

  else:
    if (A <= C <= B):
      print(int(A),",",int(C),",",int(B))

    else:
      if (B <= C <= A):
        print(int(B),",",int(C),",",int(A))

      else:
        if (C <= B <= A):
          print(int(C),",",int(B),",",int(A))
        else:
          print(int(C),",",int(A),",",int(B))            