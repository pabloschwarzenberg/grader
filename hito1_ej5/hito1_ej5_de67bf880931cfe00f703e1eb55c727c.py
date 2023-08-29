#Cálculo del dígito verificador de un rut
x=int(input())
X1=x//10000000
X2=(x//1000000)%10
X3=(x//100000)%10
X4=(x//10000)%10
X5=(x//1000)%10
X6=(x//100)%10
X7=(x//10)%10
X8=x%10
s_and_p=2*X8+3*X7+4*X6+5*X5+6*X4+7*X3+2*X2+3*X1
resto=s_and_p%11
resta=11-resto
if resta==11:
   print('dv=',0)
elif resta==10:
   print('dv=k')
else:
   print('dv=',resta)
