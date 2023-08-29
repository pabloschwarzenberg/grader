first_number=input()
second_number=input()
third_number=input()
n1=int(first_number)
n2=int(second_number)
n3=int(third_number)
if n1<=n2<=n3 :
 print(n1,"," ,n2,","  ,n3)
else :
 if n1<=n3<=n2 :
  print(n1,"," ,n3,"," ,n2)
 else:
  if n2<=n1<=n3 :
   print(n2,"," ,n1,"," ,n3)
  else :
   if n2<=n3<=n1 :
    print(n2,"," ,n3,"," ,n1)
   else:
    if n3<=n1<=n2 :
     print(n3,"," ,n1,"," ,n2)
    else:
      print(n3,"," ,n2,"," ,n1)