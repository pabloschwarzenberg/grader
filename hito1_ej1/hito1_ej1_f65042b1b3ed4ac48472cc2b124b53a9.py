#Nota final
PT=float(input())
PI=float(input())
NE=float(input())
PP=float(input())

if(1<=PT<=7) and(1<=PI<=7) and(1<=NE<=7) and(1<=PP<=7):
  NF=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print(round(NF,1))