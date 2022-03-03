x = 10

def check():
    a = 30
    print(x)
    print(a)
    return

check()
print(x)
print(a)

# 9行目で関数checkを呼び出しているため、この関数の内側の処理が実行される。
# 関数の中では変数aに30をセットした後、xとaの値が順に出力される。
# しかし、関数checkが終了した後で、xとaの値を出力しようとすると、xは出力できるが、aは定義されておらずエラーとなる。