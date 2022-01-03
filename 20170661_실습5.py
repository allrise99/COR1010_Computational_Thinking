print("20170661 조진우 실습5")

print("\n****문제 1****")          #문제 1 답안
name = input("영문이름? (이름 성)") #이름을 입력 받아 name 문자열 변수에 할당
birth = input("생일?(yyyy/mm/dd)") #생일을 입력받아 birth 문자열 변수에 할당

id1, id2 = name.split(" ") #name 변수를 공백 기준으로 split하여 이름은 id1, 성은 id2 변수에 할당
id1 = id1[1:]              #성에 해당하는 변수 id1을 문자열의 두 번째 문자부터 끝까지 슬라이싱하여 id1에 선언
id2 = id2[len(id2)-1]      #이름에 해당하는 변수 id2 문자열 맨 마지막 부분을 인덱싱하여 id2에 선언
id = id2+id1               #연결 연산자 '+'를 이용하여 id2와 id1 연결하고 이를 변수 id에 선언

by, bm, bd = birth.split("/") #변수 birth '/' 기준으로 split
psword = bd+bm+by             #split한 변수들을 역순으로 문자열 연결 연산자 이용하여 concatnate, 변수 psword에 선언

print("아이디 {}".format(id))       #포맷팅을 이용하여 문자열 변수 id 출력
print("패스워드 {}".format(psword)) #포맷팅을 이용하여 문자열 변수 id 출력

print("\n****문제 2****") #문제 2 답안
v1 = input("소중한 것?")  #input 함수로 입력 받은 문자열 v1 변수에 할당
v2 = input("소중한 것?")  #input 함수로 입력 받은 문자열 v2 변수에 할당
v3 = input("소중한 것?")  #input 함수로 입력 받은 문자열 v3 변수에 할당
v4 = input("소중한 것?")  #input 함수로 입력 받은 문자열 v4 변수에 할당
v5 = input("소중한 것?")  #input 함수로 입력 받은 문자열 v5 변수에 할당
v6 = input("소중한 것?")  #input 함수로 입력 받은 문자열 v6 변수에 할당
v7 = input("소중한 것?")  #input 함수로 입력 받은 문자열 v7 변수에 할당

print()              #줄바꿈
print(v1, end = " ") #v1 변수 출력, 끝 문자는 ' '
print(v2, end = " ") #v2 변수 출력, 끝 문자는 ' '
print(v3, end = " ") #v3 변수 출력, 끝 문자는 ' '
print(v4, end = " ") #v4 변수 출력, 끝 문자는 ' '
print(v5, end = " ") #v5 변수 출력, 끝 문자는 ' '
print(v6, end = " ") #v6 변수 출력, 끝 문자는 ' '
print(v7, end = "\n\n") #v7 변수 출력, 다음 print문 출력 결과와 한 칸 떨어져 있으므로 end 문자 \n\n 두 번 사용

#한 print문에 포맷팅 변수 %s와 개행 문자 \n를 이용하여 변수 v1~v7 각각 줄 바꿔서 출력
print("%s\n%s\n%s\n%s\n%s\n%s\n%s"%(v1, v2, v3, v4, v5, v6, v7))
