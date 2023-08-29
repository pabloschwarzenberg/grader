#Conversión de Decimal a Binario
NEL = int(input("Conversión de Decimal a Binario: "))

NAL = list(bin(NEL))
NAL.pop(0)
NAL.remove("b")

NEL = "".join(NAL)
print("resultado=",NEL)
