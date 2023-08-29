print("Orden de números enteros de menor a mayor: ")
p_n = int(input("Escribir primer número: "))
s_n = int(input("Escribir segundo número: "))
t_n = int(input("Escribir tercer número: "))

a = min(p_n, s_n, t_n) 
c = max(p_n,s_n,t_n)
b = (p_n+s_n+t_n)-c-a

print("el orden de menor a mayor de los números es: {}, {}, {}".format(a,b,c))