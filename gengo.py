# -*- coding: utf-8 -*-

#西暦の年が引数で与えられた時、元号に変換して出力する関数を作成してください。
#与えられる西暦の年は1869以上2020年いかに対応するものとします。
#なお、昭和64年→平成1年、平成31年→令和1年のように、同じ年に複数の元号が考えられる場合は、後の元号で出力するものとします。


year = input('year: ')

def gengo(year):
  if year < 1868:
    return ''
  elif year < 1912:
    return '明治' + str(year - 1867) + '年'
  elif year < 1926:
    return '大正' + str(year - 1911) + '年'
  elif year < 1989:
    return '昭和' + str(year - 1925) + '年'
  elif year < 2019:
    return '平成' + str(year - 1988) + '年'
  else:
    return '令和' + str(year - 2018) + '年'

print(gengo(year))
