#20170661 조진우

print("***문제 1***") #문제 1 답안

medals = [['Austria', 0, 2, 1], ['Canada', 4, 8, 5], ['China', 5, 0, 1], ['France', 0, 4, 5], ['Germany', 1, 1, 2],
          ['Japan', 1, 1, 0], ['Korea', 5, 3, 1], ['Norway', 4, 4, 7], ['Russia', 4, 6, 4], ['Viet Nam', 1, 1, 5]]
#medals 리스트에 각 국가 이름 및 금은동 메달 수 원소로 선언

for i in range(0, 10) : #Austria부터 Viet Nam까지
    sum = 0             #한 국가의 메달 합계를 나타내는 변수 sum
    for j in range(1, 4) :  #금은동 메달수가 나타난 1, 2, 3번째 원소에 대해
        sum += medals[i][j] #이들의 원소들을 변수 sum에 더해줌
    medals[i].append(sum)   #medals의 i번째 원소 맨 마지막 원소로 sum 값을 붙여줌
    print(medals[i])        #medals의 i번째 원소(각 국가 메달) 출력

print(medals) #medals 리스트 전체 출력

print() #indent
print("***문제 2***") #문제 2 답안
menu = {'쥬스' : '4000', '모카라떼' : '3500','아메리카노' : '2000', '카페라떼' : '3000'}
#사전형 객제 menu 선언, 메뉴 및 음료별 가격 선언
print("* 모든 메뉴:")   #출력 1. menu 변수의 key값 출력
for i in menu.keys():   #menu 변수의 key들에 대해서 반복문 실행
    print(i, end = " ") #key값 하나 출력하고 다음 값 띄어서 나오도록 선언

print()#indent
print()#indent

print("* 메뉴별 가격:")      #출력 2. menu 변수의 key, value 출력
for a, b in menu.items():   #menu 변수의 key, value 값 원소 하나씩 출력
    print(a, b+"원")         #음료 이름 및 그에 따른 가격 출력
