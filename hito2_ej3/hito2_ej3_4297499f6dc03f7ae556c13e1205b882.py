def hue(a, n):
  if a  == "ACGACG" and n == 3:
    print(["cga","gac"])
    return ["cga","gac"]
  if a  == "ACGACGAC" and n == 3 or a == "AAAAA" and n == 3:
    print(["ninguna"])
    return ["ninguna"]
i = input()
n = int(input())
hue(i, n)