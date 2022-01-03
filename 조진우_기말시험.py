#20170661 조진우 기말시험

def find_not_3times(a) :
    #1 ~ a까지 중에서 3의 배수가 아닌 정수의 개수 출력하는 함수 find_not_3times 선언
    #입력 parameter : a, return parameter : count

    count = 0                #3의 배수가 아닌 정수 개수 할당할 변수 count 0으로 선언
    for i in range(1, a+1) : #1부터 a까지 정수에 대해
        if i % 3 == 0 :      #만약 3의 배수라면
            continue         #뒤의 명령어를 건너뜀
        count += 1           #3의 배수가 아니라면 count 변수 1 증가
    return count             #count 변수값 되돌려줌


print('***문제 1***') #문제 1 출력
while(True) :    #무한 반복문 선언
    a = input()  #키보드 입력값 변수 a에 할당 
    if a == '' : #만약 빈 문자열이 입력되면
        break    #반복문 종료
    
    a = int(a) #문자열 변수 a integer로 형 변환
    result = find_not_3times(a) #함수 find_not_3times에 a input, return value 변수 result에 선언 
    print(result)   #result 변수 출력


print() #indentation
print('***문제 2***') #문제 2 출력

menu = {'김치찌개' : 6000, '된장찌개' : 6000, '제육볶음' : 8000}
#메뉴를 key, 그에 따른 가격 value로 딕셔너리 menu에 선언 

while (True) : #무한 반복문
    tmp = input("1전체메뉴 보기, 2메뉴가격 보기, 3메뉴 추가/수정, 4메뉴 삭제, 9종료\n")
    #안내 문구 출력, 입력 값을 안내 문구 밑에 받아야 하므로 끝에 \n 추가
    tmp = tmp.split()  #입력받은 문자열 공백 기준으로 split
    if tmp[0] == '9' : #만약 9를 입력했다면
        break          #반복문 종료

    if tmp[0] == '1' : #1을 입력했다면
        print(menu)    #메뉴 출력

    if tmp[0] == '2' : #입력 문자열 맨 첫부분에 2가 있을 때

        if tmp[1] in menu : #menu 변수에 입력한 메뉴가 있다면
            print("{} {}원".format(tmp[1], menu[tmp[1]]))           
            #입력한 메뉴 이름과 그 가격 출력
            
        else : #입력한 메뉴 이름이 menu 변수에 없다면
            print("{} 없음".format(tmp[1]))
            #입력한 메뉴 이름과 그 메뉴가 없다는 내용 출력
             
    if tmp[0] == '3' : #입력 문자열 맨 첫 부분에 3이 있을 때

        if tmp[1] in menu : #menu 변수에 입력한 메뉴가 있다면
            menu[tmp[1]] = int(tmp[2]) #menu 변수의 value(가격)을 입력 받은 가격으로 수정
            print("{} {}원 수정".format(tmp[1], menu[tmp[1]]))
            #입력한 메뉴 이름과 수정한 금액 출력

        else : #입력한 메뉴 이름이 menu 변수에 없다면
            menu[tmp[1]] = int(tmp[2])
            #menu 변수에 새로운 key로 입력받은 메뉴 이름 및 그에 따른 value 선언
            print("{} {}원 추가".format(tmp[1], menu[tmp[1]]))
            #추가된 메뉴와 그 가격 출력
         
    if tmp[0] == '4' : #입력 문자열 맨 첫부분에 4이 있을 때

        if tmp[1] in menu : #menu 변수에 입력한 메뉴가 있다면
            del menu[tmp[1]] #입력한 메뉴의 정보 menu 변수에서 제거 
            print("{} 삭제".format(tmp[1])) #입력한 메뉴 삭제 확인 내용 출력

        else : #입력한 메뉴 이름이 menu 변수에 없다면
            print("{} 없음".format(tmp[1])) #입력한 메뉴 없음 출력
            

        
    
