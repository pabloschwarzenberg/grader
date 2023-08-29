x = int(input("Ingresa primer digito:"))
y = int(input("Ingresa segundo digito:"))
z = int(input("Ingresa tercer digito:"))
v = min(x,y,z)
v1 = max(x,y,z)
v2 = (x+y+z)-v-v1
print("el orden es:{},{},{}". format(v,v2,v1))