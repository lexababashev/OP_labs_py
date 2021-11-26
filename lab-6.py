import math

def inputval ():
    a = float(input())
    b = float(input())
    c = float(input())
    while(a + b <= c or a + c <= b or c + b <= a or a <= 0 or b <= 0 or c <= 0):
        print("try again")
        a = float(input())
        b = float(input())
        c = float(input())
    return a, b, c

def geron_area(a , b, c):
    p = (a + b + c) / 2
    value = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return value

print("write down the sides of the first triangle:")
a1, b1, c1 = inputval()
first = geron_area(a1, b1, c1)

print("write down the sides of the second triangle:")
a2, b2, c2 = inputval()
second = geron_area(a2, b2, c2)

print("write down the sides of the third triangle:")
a3, b3, c3 = inputval()
third = geron_area(a3, b3, c3)



print("first triagle = ", first , "\n second triagle = ", second , "\n third triagle = ", third)

if (first > second and first > third):
    print("first is the biggest = ",first)

elif (second > first and second > third):
    print("second is the biggest = ", second)

elif (third > first and second < third):
    print("third is the biggest = ",third)
else:
    print("identical triangles")
