#20170661 조진우

print("***문제 1***") #문제 1 답안
tmp = int(input("월을 입력하세요: ")) #입력받는 월 tmp 변수에 할당
m = {1 : 'Jan', 2 : 'Feb', 3 : 'Mar', 4 : 'Apr', 5 : 'May', 6 : 'Jun',
     7 : 'Jul', 8 : 'Aug', 9 : 'Sep', 10 : 'Oct', 11 : 'Nov', 12 : 'Dec'}
#1~12월에 대응되는 영문이름 원소 사전형 객체 m 선언

if tmp in m:        #입력을 1~12월을 했다면
    result = m[tmp] #그에 맞는 영문이름을 result에 선언
else :              #그 외의 값을 입력했다면
    result = "오류!!" #'오류!!'라고 출력
    
print("%d월은 %s입니다."%(tmp, result)) #입력한 월과 그에 따른 결과 출력


print() #indent
print("***문제 2***") #문제 2 답안

coffee = {'쥬스' : 4000, '모카라떼' : 3500, '아메리카노' : 2000, '카페라떼' : 3000}
#사전형 객체 coffee 선언, key와 매칭되는 value 선언  
print(coffee) #출력 1. 사전형 객체 coffee 출력

a = list(coffee) #리스트형으로 형변환한 coffee를 변수 a에 선언
print('모든 메뉴', a) #출력 2. 리스트형 변수 a 출력

if '아메리카노' in coffee : #출력 3. 아메리카노가 사전형 객체 coffee에 있다면
    print("아메리카노, 메뉴에 있음") #있다고 출력
else : #없다면
    print("아메리카노, 메뉴에 없음") #없다고 출력

if '카푸치노' in coffee : #출력 4. 카푸치노가 사전형 객체 coffee에 있다면
    print("카푸치노, 메뉴에 있음") #있다고 출력
else : #없다면
    print("카푸치노, 메뉴에 없음") #없다고 출력

coffee['카푸치노'] = 3000 #사전형 객체 coffee에 카푸치노 원소 추가
del coffee['모카라떼'] #사전형 객체 coffee에 모카라떼 원소 삭제
coffee['카페라떼'] = 3500 #원소 카페라떼의 대응 value 3500원으로 새로 선언

print(coffee) #출력 5. 수정된 사전형 객체 coffee 출력
