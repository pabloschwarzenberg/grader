string=input("Ingresar secuencia: ")

sec=string.upper()
secuencia=list(sec)
bases_nitrogenadas=["A","C","G","T"]

for n in secuencia:
  if not n in bases_nitrogenadas:
    print("Secuencia Incorrecta")
  else:
    print("Secuencia Correcta")
