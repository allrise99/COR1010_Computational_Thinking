#20170661 조진우 실습 10

print("*****문제 1*****")                #문제 1 출력
print("정수를 입력하세요. 0입력시 종료!") #숫자 입력 문구
sum = 0 #정수 합 할당 변수 sum 선언
i = 0   #연산 횟수를 세는 변수 i 선언
while (True) : #무한 반복
    tmp = int(input(""))    #더할 값 tmp 변수로 입력받음
    if tmp == 0 :           #만약 입력 받은 값이 0이라면
        break               #입력 반복 종료
    sum += tmp  #입력 받은 값이 0이 아니라면 sum 변수에 tmp 값 더해줌
    i += 1      #i 하나 증가

avg = sum / i #평균을 나타내는 변수 avg 선언, 정수 총합을 연산 횟수로 나눈 값 

print('평균 %.1f'%avg) #평균 소수점 한자리에서 반올림하여 출력


print() #indentation
print('*****문제 2*****') #문제 2 출력

tmp = input('입력하세요\n')  #입력 문구 tmp에 할당
tmplen = len(tmp)           #x의 길이
s = '~!@#$%^&*-_+=(){}[]:;?.,<>' #특수문자 문자열 s에 할당
x = '' #빈 문자열 선언, tmp 문자열을 복사하여 붙여넣을 공간 

for i in range(0, tmplen) : #문자열 x의 모든 구성요소들에 대해
      if tmp[i] in s :      #만약 특수문자가 있다면
          x += ' '          #x의 해당 순서에 공백 할당
      else :                #특수문자 없을 경우
          x += tmp[i]       #문자열 tmp의 i번째 원소 변수 x에 할당

print('** 특수문자를 공백으로 바꾼 새 문자열') #특수문자 제거한 문자열 x 출력
print(x) #문자열 변수 x 출력

xsplit = x.split() #공백 기준으로 자른 x 문자열 변수 xsplit에 할당
x2 = {} #빈 dictionary 변수 x2 선언

for j in range(0, len(xsplit)) : #xsplit의 모든 원소들에 대해
    x2[xsplit[j]] = x2.get(xsplit[j], 0)+1
    #xsplit의 j번째 값이 없으면 0, 있다면 해당 값에 1을 더한 값을 x2[xsplit[j]]에 할당
    
xlist = list(x2.items()) #리스트형 변수 xlist에 x2의 원소 할당

print('** 단어별 빈도수') #xlist의 단어 빈도수 출력
for k in range(0, len(xsplit)) : #xsplit의 모든 원소들에 대해
    print('{:10}{:3}'.format(xlist[k][0], xlist[k][1])) #xlist 원소 이름과 빈도수 출력
