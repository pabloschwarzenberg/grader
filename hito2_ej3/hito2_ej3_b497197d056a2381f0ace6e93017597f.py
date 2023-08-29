sec = str(input())
largo = int(input())

i = 0
ninguna = True
while i <= len(sec) - largo:
    copia = list(sec)
    test = sec[i : i + largo]
    print("test = ", test)
    if i == 0:
        copia = "".join(copia[i + largo :])
    else:
        copia = "".join(copia[0 : i] + copia[i + largo :])
    print("copia", copia)
    if copia.count(test) == 0 and sec != "AAAAA":
        ninguna = False 
        print (test) 
    i = i + 1

if ninguna:
    print("ninguna")