#20170661 조진우 중간시험

print("***문제 1***") #문제 1번 답안
a = "Korea:Korean"      #문자열 변수 a에 Korea:Korean 할당
n1, n2 = a.split(":")   #문자열 변수 a를 ':' 구분자로 split 메소드를 이용하여 n1, n2에 할당
n3 = a[0:5]             #문자열 변수 a를 Korea나오도록 slicing하여 변수 n3에 할당
n4 = a[6:12]            #문자열 변수 a를 : 이후'Korean' 만 나오도록 slicing하여 변수 n4에 할당

print("In %s, people speak %s."%(n1, n2)) #split 메소드 이용한 결과인 문자열 n1, n2 출력
print("In %s, people speak %s."%(n3, n4)) #slicing 이용한 결과인 문자열 n3, n4 출력

print()               #문제 2번 가독성을 위한 space
print("***문제 2***") #문제 2번 답안
word = input("5글자 단어입력?") #입력받은 문자열 word 변수에 할당
vowel = "aeiouAEIOU"           #문자열 변수 vowel에 모음 10글자 할당 (대문자 포함)

if word[0] in vowel : #word의 첫번째 글자가 모음인 경우
    newword = word+'ay' #word 바로 뒤에 ay를 붙인 새 문자열 변수 newword를 선언

elif word[1] in vowel: #word의 두번째 글자가 모음인 경우
    tmp = word[0]      #임시 문자열 변수 tmp에 word 첫 글자 할당
    newword = word[1:5]+tmp+'ay' #새 문자열 변수 newword에 첫 글자 제외한 word slicing 한 것과 tmp, 'ay' 연결하여 선언

elif word[2] in vowel: #word의 세번째 글자가 모음인 경우 
    tmp = word[0:1]     #임시 문자열 변수 tmp에 word의 첫 두 글자 할당
    newword = word[2:5]+tmp+'ay' #새 문자열 변수 newword에 첫 두 글자 제외한 word slicing 한 것과 tmp, 'ay' 연결하여 선언
    
elif word[3] in vowel: #word의 세 번째 글자가 모음인 경우
    tmp = word[0:2]     #임시 문자열 변수 tmp에 word의 첫 세 글자 할당
    newwword = word[3:5]+tmp+'ay' #새 문자열 변수 newword에 첫 세 글자 제외한 word slicing 한 것과 tmp, 'ay' 연결하여 선언
    
elif word[4] in vowel: #word의 네 번째 글자가 모음인 경우
    tmp = word[0:3]     #임시 문자열 변수 tmp에 word의 첫 네 글자 할당
    newword = word[4:5]+tmp+'ay' #새 문자열 변수 newword에 첫 네 글자 제외한 word 변수 slicing한 것과 tmp, 'ay' 연결하여 선언 

print("%s->%s"%(word, newword)) #word, newword 변수 출력

print()              #문제 3번 가독성을 위한 space
print("***문제 3***") #문제 3번 답안
day = input("오늘의 요일?") #day 변수에 요일 할당
date = input("오늘부텨 경과한 일수를 입력?") #date 변수에 경과 일수 입력
date = int(date) #문자열 변수인 date을 정수형으로 형변환

d = "월화수목금토일" #요일을 확인할 문자열 변수 d 선언
temp = date % 7 #date를 7 나눠 나온 나머지 값인 temp 선언

if day in d[0] : #입력받은 요일이 월요일일 경우
    i = 0 #임시 변수 i 할당
    i += temp #temp 변수 값을 i에 더해줌
    if i >= 7 : #i 값이 7보다 클 경우 (주가 바뀔 경우)
        i %= 7 #다시 7로 나는 나머지 값을 i에 할당
        fdate = d[i] #미래의 요일 나타내는 변수 fdate는 문자열 d의 i번째 요소
    else : #주가 바뀌지 않는 경우 
        fdate = d[i]  #fdate는 문자열 d의 i번째 요소

elif day in d[1] : #입력받은 요일이 화요일일 경우
    i = 1 #임시 변수 i 할당
    i += temp #temp 변수 값을 i에 더해줌
    if i >= 7 : #i 값이 7보다 클 경우 (주가 바뀔 경우)
        i %= 7 #다시 7로 나는 나머지 값을 i에 할당
        fdate = d[i] #미래의 요일 나타내는 변수 fdate는 문자열 d의 i번째 요소
    else : #주가 바뀌지 않는 경우 
        fdate = d[i]  #fdate는 문자열 d의 i번째 요소

elif day in d[2] : #입력받은 요일이 수요일일 경우
    i = 2 #임시 변수 i 할당
    i += temp #temp 변수 값을 i에 더해줌
    if i >= 7 : #i 값이 7보다 클 경우 (주가 바뀔 경우)
        i %= 7 #다시 7로 나는 나머지 값을 i에 할당
        fdate = d[i] #미래의 요일 나타내는 변수 fdate는 문자열 d의 i번째 요소
    else : #주가 바뀌지 않는 경우 
        fdate = d[i]  #fdate는 문자열 d의 i번째 요소

elif day in d[3] : #입력받은 요일이 목요일일 경우
    i = 3 #임시 변수 i 할당
    i += temp #temp 변수 값을 i에 더해줌
    if i >= 7 : #i 값이 7보다 클 경우 (주가 바뀔 경우)
        i %= 7 #다시 7로 나는 나머지 값을 i에 할당
        fdate = d[i] #미래의 요일 나타내는 변수 fdate는 문자열 d의 i번째 요소
    else : #주가 바뀌지 않는 경우 
        fdate = d[i]  #fdate는 문자열 d의 i번째 요소

elif day in d[4] : #입력받은 요일이 금요일일 경우
    i = 4 #임시 변수 i 할당
    i += temp #temp 변수 값을 i에 더해줌
    if i >= 7 : #i 값이 7보다 클 경우 (주가 바뀔 경우)
        i %= 7 #다시 7로 나는 나머지 값을 i에 할당
        fdate = d[i] #미래의 요일 나타내는 변수 fdate는 문자열 d의 i번째 요소
    else : #주가 바뀌지 않는 경우 
        fdate = d[i]  #fdate는 문자열 d의 i번째 요소
    
elif day in d[5] : #입력받은 요일이 토요일일 경우
    i = 5 #임시 변수 i 할당
    i += temp #temp 변수 값을 i에 더해줌
    if i >= 7 : #i 값이 7보다 클 경우 (주가 바뀔 경우)
        i %= 7 #다시 7로 나는 나머지 값을 i에 할당
        fdate = d[i] #미래의 요일 나타내는 변수 fdate는 문자열 d의 i번째 요소
    else : #주가 바뀌지 않는 경우 
        fdate = d[i]  #fdate는 문자열 d의 i번째 요소
        
elif day in d[6] : #입력받은 요일이 일요일일 경우
    i = 6 #임시 변수 i 할당
    i += temp #temp 변수 값을 i에 더해줌
    if i >= 7 : #i 값이 7보다 클 경우 (주가 바뀔 경우)
        i %= 7 #다시 7로 나는 나머지 값을 i에 할당
        fdate = d[i] #미래의 요일 나타내는 변수 fdate는 문자열 d의 i번째 요소
    else : #주가 바뀌지 않는 경우 
        fdate = d[i]  #fdate는 문자열 d의 i번째 요소
 
print("오늘은 %s요일, %d일 후는 %s요일"%(day, date, fdate)) #오늘의 요일 문자열 변수 day, 미래 일수 나타내는 정수형 변수 date, 미래의 요일 문자열 변수 fdate 출력


