# -*- coding: utf-8 -*-

#1950年から2050年までの間にある「うるう年」を出力するプログラムを作成してください。
#なおうるう年は次の条件で判定できます。
#・４で割り切れる年はうるう年
#・正し、１００で割り切れて４００で割り切れない年はうるう年でない


def is_leap_year(year):
  if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
      return False
    else:
      return True

  else:
    return False

for i in range(1950, 2051):
  print(str(i) + ' ' + str(is_leap_year(i)))

