#verificador de rut
rut = input("Ingrese RUT/RUN: ")
rutLength = len(rut)
if(rutLength == 7):
  rut7 = rut[rutLength - 1]
  rut6 = rut[rutLength - 2]
  rut5 = rut[rutLength - 3]
  rut4 = rut[rutLength - 4]
  rut3 = rut[rutLength - 5]
  rut2 = rut[rutLength - 6]
  rut1 = rut[rutLength - 7]
  rutA = eval(rut7) * 2
  rutB = eval(rut6) * 3
  rutC = eval(rut5) * 4
  rutD = eval(rut4) * 5
  rutE = eval(rut3) * 6
  rutF = eval(rut2) * 7
  rutG = eval(rut1) * 2
  sumRut = rutA + rutB + rutC + rutD + rutE + rutF + rutG
elif(rutLength == 8):
  rut7 = rut[rutLength - 1]
  rut6 = rut[rutLength - 2]
  rut5 = rut[rutLength - 3]
  rut4 = rut[rutLength - 4]
  rut3 = rut[rutLength - 5]
  rut2 = rut[rutLength - 6]
  rut1 = rut[rutLength - 7]
  rut0 = rut[rutLength - 8]
  rutA = eval(rut7) * 2
  rutB = eval(rut6) * 3
  rutC = eval(rut5) * 4
  rutD = eval(rut4) * 5
  rutE = eval(rut3) * 6
  rutF = eval(rut2) * 7
  rutG = eval(rut1) * 2
  rutH = eval(rut0) * 3
  sumRut = rutA + rutB + rutC + rutD + rutE + rutF + rutG + rutH
rutDivide = sumRut // 11
rutDiff = sumRut - (11 * rutDivide)
finalModule = 11 - rutDiff
if(finalModule == 11):
  print("dv=0")
elif(finalModule == 10):
  print("dv=K")
else:
  print("dv={}".format(finalModule))