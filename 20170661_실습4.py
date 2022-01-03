print('\n 조진우 20170661 실습4')   #인적사항 출력
print('\n****문제1****')         #문제 1 답안 출력

msg = '공부 사랑 돈 부모님 건강 친구 재미'    #문자열 변수 msg 선언
v1, v2, v3, v4, v5, v6, v7 = msg.split(' ') #공백 기준으로 분리한 문자열 v1 ~ v7에 선언
print(v1) #변수 v1 출력
print(v2) #변수 v2 출력
print(v3) #변수 v3 출력
print(v4) #변수 v4 출력
print(v5) #변수 v5 출력
print(v6) #변수 v6 출력
print(v7) #변수 v7 출력
print(v1, v2, v3, v4, v5, v6, v7) #변수 v1~v7 한꺼번에 출력

print('\n****문제2****')  #문제 2 답안 출력

name = 'Geppert Nam'      #문자열 변수 name에 이름 선언
birth = '1960/04/18'      #문자열 변수 birth에 생년월일 선언
n1tmp, n2tmp = name.split(' ')     #공백 기준으로 변수 name split
n1tmp = n1tmp[1:]                  #n1tmp의 두 번째 알파벳부터 끝까지 Slicing 하여 n1tmp에 선언 
n2tmp = n2tmp[len(n2tmp)-1:]       #len 함수 이용하여 n2tmp의 마지막 알파벳만 Slicing, n2tmp에 선언
id = n2tmp+n1tmp                 #문자열 변수 id에 Slicing 한 변수 n2tmp와 n1tmp concatnate

tmp1, tmp2, tmp3 = birth.split('/')  # '/' 기준으로 birth 변수 split, tmp1, tmp2, tmp3에 할당
psword = tmp3+tmp2+tmp1              # 변수 psword에 tmp3, tmp2, tmp1 concatnate
print('이름', name)       #문자열 변수 name 출력
print('아이디', id)       #n2tmp와 n1tmp concatnate한 문자열 변수 id 출력
print('생년월일', birth)  #문자열 변수 birth 출력
print('패스워드', psword) #tmp3와 tmp2, tmp1 concatnate한 문자열 변수 psword 출력
