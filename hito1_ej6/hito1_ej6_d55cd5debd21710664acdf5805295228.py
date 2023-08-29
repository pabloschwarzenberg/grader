A=int(input("ingrese numero 1  : "))
B=int(input("ingrese numero 2  : "))
C=int(input("ingrese numero 3  : "))
if(A<=B<=C):
  print(str(A)+","+str(B)+","+str(C))
elif(A<=C<=B):
  print(str(A)+","+str(C)+","+str(B))
elif(B<=A<=C):
  print(str(B)+","+str(A)+","+str(C))
elif(B<=C<=A):
  print(str(B)+","+str(C)+","+str(A))
elif(C<=A<=B):
  print(str(C)+","+str(A)+","+str(B))
elif(C<=B<=A):
  print(str(C)+","+str(B)+","+str(A))
      