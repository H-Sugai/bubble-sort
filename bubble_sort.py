import random

a = int(input("データ数を入力してください:"))
data = [random.randint(0, 100) for i in range(a)]
print(data)
b = input("昇順ですか？降順ですか？")

if b == "昇順":
    for i in range(1, len(data)):
        for j in range(0, len(data) - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    print(data)

elif b == "降順":
    for i in range(1, len(data)):
        for j in range(0, len(data) - i):
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    print(data)

else:
    print("正しく入力してください")

