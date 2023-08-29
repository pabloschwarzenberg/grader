#Ordenar tres números
n1 = int(input("Coloque el primer número:"))
n2 = int(input("Coloque el segundo número"))
n3 = int(input("Coloque el tercer numero"))

mini = min(n1, n2, n3)
maxi = max(n1, n2, n3)
me = (n1+n2+n3)-mini-maxi
print(mini,",",me,",",maxi)