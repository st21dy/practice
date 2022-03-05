n = '10010'

result = 0
for i in range(len(n)):
  result += int(n[i]) * (2 ** (len(n) - i - 1))

print(result)



a = 0b10010
print(a)



b = '10010'
print(int(b, 2))
