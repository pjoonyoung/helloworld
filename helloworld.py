pi = 3.14
def circle(x):
    return x * x * pi
def square_area(x,y):
    return x * y
def triangel_area(x,y):
    return (x * y) / 2

figure = 0
while figure != 4:
    figure = int(input ("1.삼각형\n2.사각형\n3.원\n4.종료\n번호선택:"))
    if figure == 1:
        width = int(input('밑변:'))
        heigh = int(input('높이:'))
        print ('넓이',triangel_area(width,heigh))
    elif figure == 2:
        width = int(input('가로:'))
        heigh = int(input('세로:'))
        print('넓이', square_area(width, heigh))
    elif figure == 3:
        radius = int(input('반지름:'))
        print('넓이', circle(radius))
    elif figure == 4:
        print('종료합니다.')
    else:
        print('올바른숫자를 입력해주세요.')

# for문 구구단생성

for i in range(2,10):
    print("구구단수:", i)
    for j in range(1,10): # 1~9까지 반복
        print(f"{i}*{j} = {i*j}") # 1 * 1 = 1, 1 * 2 = 2, 1 * 3 = 3 ~ 1 * 9 = 9

#클래스를 활용한 원넓이 공식

import math

class Circle:
    color = "red"

    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def area(self):
        return self.radius * self.radius * math.pi