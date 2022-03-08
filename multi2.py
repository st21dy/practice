# -*- coding: utf-8 -*-

# 体積を求める計算量

n = 10

for i in range(1, n):
  for j in range(1, n):
    for k in range(1, n):
      print(str(i) + '*' + str(j) + '*' + str(k) + '=' + str(i * j * k))

