a = input(">>> ")
flag = True
for x in a:
    if x in "ACTG":
        pass
    else:
        flag = False
if flag:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")