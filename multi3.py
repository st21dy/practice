# -*- coding: utf-8 -*-

# 身長と体重からBMI（肥満度を示す体格指数）を求める関数

# BMIを計算(体重[kg], 身長[m])
def calc_bmi(weight, height):
  return round(weight / (height ** 2))

# BMI値 → 判定結果
def bmi_to_result(bmi):
  if bmi < 18.5:
    return "痩せぎみ"
  elif (bmi >= 18.5) and (bmi < 25):
    return "標準"
  elif (bmi >= 25) and (bmi < 30):
    return "肥満ぎみ"
  else:
    return "肥満"

height = input('height(m): ')
weight = input('weight(kg): ')

bmi = calc_bmi(weight, height)

# BMI値 → 判定結果
result = bmi_to_result(bmi)

# 結果表示
print('BMI: ' + str(bmi))
print('判定結果: ' + str(result))