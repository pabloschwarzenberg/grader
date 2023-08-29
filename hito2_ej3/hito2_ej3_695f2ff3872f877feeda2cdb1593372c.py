def main():
  s1 = input("Enter first strand: ")
  s2 = input("Enter second strand: ")
  window = 0
  if len(s1) < len(s2):
    window = len(s1)
  elif len(s1) > len(s2):
    window = len(s2)
  else:
    window = len(s1)
  for i in range(window, 1, -1):
    for j in range(0, i, 1):
      if s1.find(s1[i:i + window]) == s2.find(s2[i:i + window]):
        max = a[0][0]
        for i in range(len(a)):
            for j in range(len(a[i]):
                if (a[i][j] > max):
                    max = a[i][j]
                    print ("Common Subsequence: ", max)
      else:
        print ("No Common Sequence Found")

main()