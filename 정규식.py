
import re

data = "asdfsfhd51sg51s65g14s6f5g4165sg1451651"

# newdata = re.sub(r'[0-9]+','',data) # 숫자를 제외한 값 반환
newdata = re.sub(r'[^0-9]+','',data) # 숫자 외 것들을 제외한 값 반환
print(newdata)

data1 = "asdfsfh@#$d51sg@#51s65g14s@#$6f@#5g41#$65sg1451651"

# newdata1 = re.sub('[@#$]','',data1) # 특수문자를 제외한 값 반환
newdata1 = re.sub('[^@#$]','',data1)# 특수문자 외 것들을 제외한 값 반환
print(newdata1)

data2 = "안!@##1315녕asdfsad하23!@$세!@#asd요@#$"
# newdata2 = re.sub('[ㄱ-ㅣ가-힣]','',data2) # 한글을 제외한 값 반환
newdata2 = re.sub('[^ㄱ-ㅣ가-힣]','',data2)# 한글 외 것들을 제외한 값 반환
print(newdata2)