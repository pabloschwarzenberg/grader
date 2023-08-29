n=int(input("Ingrese un número: "))
u= n/1000
t= n%1000
c= t/100
t= t % 100
dec= t/10
un= t%10
print (" %i" % u,"M","+"," %i" % c,"C","+"," %i" % dec,"D","+"," %i" % un,"U")