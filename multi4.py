# -*- coding: utf-8 -*-

# 円周率Πの近似値を求める関数
# （n✖︎nの正方形農地、扇型の範囲内に入る数を数える）


def pi(n):
  cut = 0
  for i in range(n):
    for j in range(n):
      # 三平方の定理により扇型の内部か判定
      if i * i + j * j <= n * n:
        cnt += 1
      
      # 扇型から円に変換するため４倍する
      return cnt * 4 / (n * n)


