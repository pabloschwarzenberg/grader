#Benjamin Garcia
n1=int(input("ingrese primer valor"))
n2=int(input("ingrese segundo valor"))
n3=int(input("ingrese tercer valor"))

a=min(n1,n2,n3)

c=max(n1,n2,n3)

b=(n1+n2+n3) -a-c
print("los números ordenados de mayor a menor son", (a,b,c))