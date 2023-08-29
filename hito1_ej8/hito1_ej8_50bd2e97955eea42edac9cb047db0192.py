a = str(input("ingrese numero:"))

A = eval (a)

b = a [0:1]

c = a [1:2]

d = a [2:3]

e = a [3:4]

if (A >= 0) and (A<10):
    print (b+"U")

elif (A >= 10) and (A < 100):
    print (b+"D", "+" , c+"U")

elif (A >= 100) and (A < 1000):
    print (b+"C", "+" , c+"D", "+" , d+"U")

elif (A >= 1000) and (A < 10000):
    print (b+"M", "+" , c+"C", "+" , d+"D" , "+" , e+"U")

      