x = 10

def update():
  x += 30
  print(x)

update()
print(x)

#4行目で更新しようとした変数xがグローバル変数ではなく、ローカル変数として認識しているため、xが定義されていないとしてエラー