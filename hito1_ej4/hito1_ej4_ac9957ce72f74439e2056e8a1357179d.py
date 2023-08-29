#Conversión de Decimal a Binario
def binaryConvert(number):
  intDivide = number
  binaryNum = ""
  while not(intDivide == 0):
    modulo = intDivide%2
    intDivide = intDivide//2
    stringModulo = str(modulo)
    binaryNum += stringModulo
  print("resultado={}".format(binaryNum[::-1]))

binaryConvert(int(input("Number to convert: ")))