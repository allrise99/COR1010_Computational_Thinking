#20170661 조진우 실습7

print("***문제 1***") #문제1 답안

month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] #month 리스트 변수에 1~12월 영문 표기 원소로 선언

a = input("월을 입력하세요: ") #월 입력 받아 a 변수에 선언
a = int(a) #문자열 변수 a를 정수형으로 변환
tmp = a - 1 #리스트의 인덱싱을 위해 tmp 변수에 a-1 선언
print("%d월은 %s입니다."%(a, month[tmp])) #결과 출력

print() #indentation
print("***문제 2***") #문제 2 출력

medals = [['Austria', 0, 2, 1],['Canada', 4, 8, 5],['China', 5, 0, 1],
          ['France', 0, 4, 5],['Germany', 1, 1, 2],['Japan', 1, 1, 0],
          ['Korea', 5, 3, 1],['Norway', 4, 4, 7],['Russia', 4, 6, 4],['Viet Nam', 1, 1, 5]]
'''         medals 리스트 변수에 오스트리아, 캐나다, 중국, 프랑스, 독일,
            일본, 한국, 노르웨이, 러시아, 베트남의 국가명과 각 국가의 금은동 메달 수 원소로 선언 '''

aumedal = medals[0][1] + medals[0][2] + medals[0][3] #오스트리아 총 메달수 나타내는 aumedal에 금, 은, 동 메달 수 합산한 값 선언
medals[0].append(aumedal) #medals 리스트의 0번째 원소 맨 끝에 aumedal 값 concatenate

camedal = medals[1][1] + medals[1][2] + medals[1][3] #캐나다 총 메달수 나타내는 camedal에 금, 은, 동 메달 수 합산한 값 선언
medals[1].append(camedal) #medals 리스트의 1번째 원소 맨 끝에 camedal 값 concatenate

chmedal = medals[2][1] + medals[2][2] + medals[2][3] #중국 총 메달수 나타내는 chmedal에 금, 은, 동 메달 수 합산한 값 선언
medals[2].append(chmedal) #medals 리스트의 2번째 원소 맨 끝에 chmedal 값 concatenate

frmedal = medals[3][1] + medals[3][2] + medals[3][3] #프랑스 총 메달수 나타내는 frmedal에 금, 은, 동 메달 수 합산한 값 선언
medals[3].append(frmedal) #medals 리스트의 3번째 원소 맨 끝에 frmedal 값 concatenate

gmmedal = medals[4][1] + medals[4][2] + medals[4][3] #독일 총 메달수 나타내는 gmmedal에 금, 은, 동 메달 수 합산한 값 선언
medals[4].append(gmmedal) #medals 리스트의 4번째 원소 맨 끝에 gmmedal 값 concatenate

jpmedal = medals[5][1] + medals[5][2] + medals[5][3] #일본 총 메달수 나타내는 jpmedal에 금, 은, 동 메달 수 합산한 값 선언
medals[5].append(jpmedal) #medals 리스트의 5번째 원소 맨 끝에 jpmedal 값 concatenate

krmedal = medals[6][1] + medals[6][2] + medals[6][3] #한국 총 메달수 나타내는 krmedal에 금, 은, 동 메달 수 합산한 값 선언
medals[6].append(krmedal) #medals 리스트의 6번째 원소 맨 끝에 krmedal 값 concatenate

nwmedal = medals[7][1] + medals[7][2] + medals[7][3] #노르웨이 총 메달수 나타내는 nwmedal에 금, 은, 동 메달 수 합산한 값 선언
medals[7].append(nwmedal) #medals 리스트의 7번째 원소 맨 끝에 nwmedal 값 concatenate

rumedal = medals[8][1] + medals[8][2] + medals[8][3] #러시아 총 메달수 나타내는 rumedal에 금, 은, 동 메달 수 합산한 값 선언
medals[8].append(rumedal) #medals 리스트의 8번째 원소 맨 끝에 rumedal 값 concatenate

vnmedal = medals[9][1] + medals[9][2] + medals[9][3] #베트남 총 메달수 나타내는 vnmedal에 금, 은, 동 메달 수 합산한 값 선언
medals[9].append(vnmedal) #medals 리스트의 9번째 원소 맨 끝에 vnmedal 값 concatenate

print(medals[0]) #medals 리스트 첫 원소 출력 (국가명, 금은동 메달 수, 총 메달 개수)
print(medals[1]) #medals 리스트 두 번째 원소 출력 
print(medals[2]) #medals 리스트 세 번째 원소 출력 
print(medals[3]) #medals 리스트 네 번째 원소 출력
print(medals[4]) #medals 리스트 다섯 번째 원소 출력
print(medals[5]) #medals 리스트 여섯 번째 원소 출력
print(medals[6]) #medals 리스트 일곱 번째 원소 출력
print(medals[7]) #medals 리스트 여덟 번째 원소 출력
print(medals[8]) #medals 리스트 아홉 번째 원소 출력
print(medals[9]) #medals 리스트 열 번째 원소 출력
print()         #indentation
print(medals) #medals 리스트 전체 원소 출력
