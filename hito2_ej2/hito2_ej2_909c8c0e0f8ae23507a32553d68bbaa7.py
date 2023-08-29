def genoma(n):
    if ("A" in list(n) and "C" in list(n) and "T" in list(n) and "G" in list(n)):
        if "B" in list(n):
            return False
        return True
    else:
        return False
sec=input()
a = sec.upper()
if genoma(a) == True:
   print ("secuencia correcta")
elif genoma(a) == False:
   print ("secuencia incorrecta")