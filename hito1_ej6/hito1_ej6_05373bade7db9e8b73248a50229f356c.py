#Ordenar tres números
s=int(input())
f=int(input())
g=int(input())
if s<=f and f<=g:
   print(s,",",f,",",g)
elif g<=f and f<=s:
   print(g,",",f,",",s)
elif f<=s and s<=g:
   print(f,",",s,",",g)
elif s<=g and g<=f:
   print(s,",",g,",",f)
elif g<=s and s<=f:
   print(g,",",s,",",f)
elif f<=g and g<=s:
   print(f,",",g,",",s)