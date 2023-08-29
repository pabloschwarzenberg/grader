n1= eval(input("5"))
n2= eval(input("15"))
n3= eval(input("3"))
a= max(n1,n2,n3)
b= min(n1,n2,n3)
c= (n1 + n2 + n3) - a - b
print("{},{},{}".format(b,c,a))