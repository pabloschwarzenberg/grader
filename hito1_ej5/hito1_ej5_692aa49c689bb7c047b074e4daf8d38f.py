a = int(input("ingrese su rut:"))

i = (a%10000000000)//10000000

b = (a%10000000)//1000000

c = (a%1000000)//100000

d = (a%100000)//10000

e = (a%10000)//1000

f = (a%1000)//100

g = (a%100)//10

h = (a%10)//1

print(i)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)



h = h*2

g = g*3

f = f*4

e = e*5

d = d*6

c = c*7

b = b*2

i = i*3

print(i)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)



x = (h+g+f+e+d+c+b+i)

print(x)

z = (x//11)

print(z)

m = x-(11*z)
print(m)

n = (11-m)
print(n)


if (n==11):
    print("dv=0")

if (n==10):
    print("dv=K")

if (n!=10)and(n!=11):
    print("dv=",n)

