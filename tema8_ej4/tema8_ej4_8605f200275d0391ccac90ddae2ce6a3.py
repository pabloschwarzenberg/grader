def rot_13():
  plb = input()
  rot13 = str.maketrans(
  "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
  "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
  return print(plb.translate(rot13))