import datetime
import random

# print(random.random()) # 임의 실수 반환

# print(random.uniform(3,4)) # 3~4 사이의 임의의 실수를 반환

# print(random.randint(1,45)) # 1~45 사이의 임의의 정수를 반환(1 <= n <=45)

# for i in range(3): # 3회전
#    print(random.gauss(1,1.0)) # 가우스 분포

now = datetime.datetime.now()

random.seed (int,now)

print(random.randrange(20))

random_list = [random.randrange(45) for i in range(6)]
print(random_list)
