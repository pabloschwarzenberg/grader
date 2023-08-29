n=input()
if len(n)==4:
    print(n[:1],"M +",n[1:2],"C +",n[2:3],"D +",n[3:],"U")
elif len(n)==3:
    print(n[:1],"C +",n[1:2],"D +",n[2:],"U")
elif len(n)==2:
    print(n[:1],"D +",n[1:2],"U")
else:
    print(n[:1],"U")
