#Ordenar tres números
A=int(input())
B=int(input())
C=int(input())
if((A<=B) and (A<=C)):  
    menor=A
    if(B<=C):
      medio=B
      mayor=C
    else:
      medio=C
      mayor=B
elif((B<=A) and (B<=C)): 
    menor=B
    if(A<=C):
       medio=A
       mayor=C
    else:
       medio=C
       mayor=A
else:
  menor=C
  if(A<=B):
     medio=A
     mayor=B
  else:
     medio=B
     mayor=A
print(str(menor)+","+str(medio)+","+str(mayor))   