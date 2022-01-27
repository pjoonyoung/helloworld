import datetime

now = datetime.datetime.now() # 현재시간 불러오기
print(now)
now1 = now.strftime('%Y-%m-%d') # 년 - 월 - 일
print(now1)
now2 = now.strftime('%H-%M-%S')# 시 - 분 - 초
print(now2)
now3 = now.strftime('%Y-%m-%d %H-%M-%S')
print(now3)

