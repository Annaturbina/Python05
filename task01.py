def Power(a, b):
  result = 1
  for i in range(b):
    result = result*a
  return result

a = int(input())
b = int(input())

print(Power(a, b))