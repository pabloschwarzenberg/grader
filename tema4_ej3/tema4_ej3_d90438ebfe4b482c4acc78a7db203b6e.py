def jerigonzo(string):
  x = ""
  for i in string:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
      x += i
      x += "p"
      x += i
    else:
      x += i
  return x

if __name__ == "__main__":
  Var_1 = input()
  jerigonzo(Var_1)