#Ordenar tres números
A=int(input())
B=int(input())
C=int(input())

if  (A <= B <= C) == True:
  int(print(A,str(","),B,str(","),C))
elif (A <= C <= B) == True:
   print(A,str(","),C,str(","),B)
elif (C <= A <= B) == True:
   print(C,str(","),A,str(","),B)
elif (C <= B <= A) == True:
   print(C,str(","),B,str(","),A)
elif (B <= A <= C) == True:
   print(B,str(","),A,str(","),C)
else:
   print(B,str(","),C,str(","),A)
