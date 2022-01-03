print("20170661 조진우 실습6")

print("**** 문제 1 ****") #문제 1 출력
import keyword            #keyword 모듈 import
num = "0123456789"        #변수 이름 첫 글자가 숫자인지 확인할 용도의 문자열
tmp = input("사용할 변수 이름??") #tmp 문자열 변수에 사용할 변수 이름 입력 받음

if tmp == "" :                  #예외 처리 1 : 아무것도 입력 안하고 Enter 친 경우 
    print("이름을 입력하세요!")  #경고문 출력

else :                          #예외 처리 2 : 키보드 입력을 하고서 Enter를 친 경우
    if tmp in keyword.kwlist :  #파이썬 지정 단어 예외처리
        print("사용할 수 없음!") #경고문 출력

    elif " " in tmp :           #예외 처리 3 :변수 이름에 공백이 들어간 경우
        print("사용할 수 없음!") #경고문 출력

    elif tmp[0] in num :        #예외 처리 4 :변수 이름 맨 첫 문자가 숫자인 경우
        print("사용할 수 없음!") #경고문 출력

    elif '!' in tmp or\
         '@' in tmp or\
         '#' in tmp or\
         '$' in tmp or\
         '%' in tmp or\
         '&' in tmp or\
         '*' in tmp :           #예외 처리 5 :변수 이름에 특수문자 '!','@','#','$','%','&', '*'를 입력했을 경우
            print("사용할 수 없음!") #경고문 출력

    else :                  #위 모든 예외에 걸리지 않는 변수 이름을 입력한 경우
        print("사용 가능!") #사용 가능 출력

