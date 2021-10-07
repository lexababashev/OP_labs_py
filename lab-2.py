print("задайте размеры кирпича")
a = input()
b = input()
c = input()

print("задайте размеры прямоугольного отверстия")
x = input()
y = input()

result = None

if a < x and b < y or a < y and b < x:
    result = True

elif a < x and c < y or a < y and c < x:
    result = True

elif b < x and c < y or b < y and c < x:
    result = True
else:
    result = False

if result:
    print("пройдет")
else:
    print("не пройдет")
