#Descomponer un número
x=int(input(':'))

f=x//1000
e=x%1000//100
g=x%1000%100//10
h=x%1000%100%10//1

print(str(f)+'M',"+",str(e)+"C","+",str(g)+"D","+",str(h)+"U")
      