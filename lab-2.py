print("задайте размеры кирпича")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

print("задайте размеры прямоугольного отверстия")
x = int(input("x="))
y = int(input("y="))

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
