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

