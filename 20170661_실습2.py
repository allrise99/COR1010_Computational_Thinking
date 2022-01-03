print("20170661 조진우 실습2")

print("\n***문제1***")
cel=26                              #섭씨 온도를 나타내는 int형 변수 cel
far=(cel*1.8)+32                    #화씨 온도를 나타내는 float형 변수 far
print(far)                          
print(round(far,1))                 #소수 첫째자리에서 반올림한 변수 far 출력
print("화씨"+str(round(far,1))+"도") # + 연산자를 이용한 문자열 concatenate 및 출력

print("\n\n***문제2***")
var="공부 사랑 돈 부모님 건강 친구 재미" #문자열 변수 var 선언
print('var', var)                   #변수 이름 'var'과 변수 var의 내용 출력
print("@내게 소중한 것 7가지?")        #해당 문자열 print 함수 통해 출력
print(var)                          #변수 var의 내용 한 번 더 출력

print("\n\n***문제3***")
v1='공부'
v2='사랑'
v3='돈'
v4='부모님'
v5='건강'
v6='친구'
v7='재미' #v1 ~ v7 문자열 변수로 선언

print('v1',v1)
print('v2',v2)
print('v3',v3)
print('v4',v4)
print('v5',v5)
print('v6',v6)
print('v7',v7)              #문자열 변수 v1~v7 줄 바꿔서 출력
print("@내게 소중한 것 7가지?")
print(v1,v2,v3,v4,v5,v6,v7) #문자열 변수를 한 줄에 출력