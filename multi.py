# -*- coding: utf-8 -*-

# 掛け算の計算量を調べる

n = 10
for i in range(1, n):
  for j in range(1, n):
    print(str(i) + '*' + str(j) + '=' + str(i * j))

