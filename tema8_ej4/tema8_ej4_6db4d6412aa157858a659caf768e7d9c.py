import string
def rot13(name):
  rot12 = str.maketrans(
      'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
      'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
  return name.translate(rot12)
 
if __name__ == "__main__":
  rot13(str(input()))