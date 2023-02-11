def Sum(a, b):
  if a == 0:
    return b
  elif a > 0:
    return Sum(a - 1, b + 1)
  else:
    return Sum(a + 1, b - 1)

a = int(input())
b = int(input())
print(Sum(a, b))