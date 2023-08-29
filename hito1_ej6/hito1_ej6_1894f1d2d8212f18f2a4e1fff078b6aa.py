#Ordenar tres números
w = int(input("escriba el primer numero:"))
a = int(input("escriba el segundo numero:"))
d = int(input("escriba el tercer numero:"))
g = min(w,a,d)
f = max(w,a,d)
b =(w + a + d)-g-f
print("los numero ordenados son:{},{},{}". format(g,b,f))