x= int(input())
U=x%10
x1=x//10
D=x1%10
x2=x1//10
C=x2%10
x3=x2//10
M=x3%10

if 0==M and 0!=D and 0!=C and 0!=U:
    print(C,"C+",D,"D+",U,"U+")
if 0==M and 0==C and 0!=D and 0!=U:
    print(D,"D+",U,"U")
if 0==M==C==D and U!=0:
    print(U,"U")
else:
    print(M,"M+",C,"C+",D,"D+",U,"U")
