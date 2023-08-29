gen=input("Ingrese secuencia: ")
gen=gen.upper()
genomas=["A","C","T","G"]
lg=len(gen)
for i in range(lg):
    if gen[i] in genomas:
        continue
    else:
        print("incorrecta")
print("correcta")