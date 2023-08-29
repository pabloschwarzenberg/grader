inputNumber = int(input("Escribe un numero:"))
newInput = inputNumber
arrPrimos = []
realArrPrimos = []
i = 1
while i <= inputNumber:
    newInput = newInput - 1
    # print(i)
    if inputNumber % i == 0:
        if i != 1:
            #if i != inputNumber:
            arrPrimos.append(i)
    i = i + 1

    ii = 0
    # print('mi arr:::', arrPrimos)
    for element in arrPrimos:
        # print('evaluando element:::', element)
        if element != 2:
            if element % 2 == 0:
                arrPrimos.remove(element)
            else:
                ii = element
                # print(ii)
                while ii > 2:
                    ii = ii - 1
                    # print(ii)
                    if element % ii == 0:
                        if element in arrPrimos:
                            # print('element:::', element)
                            arrPrimos.remove(element)
for num in arrPrimos:
  print(num)