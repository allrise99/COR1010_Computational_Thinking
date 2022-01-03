#실습 11

def avg(l) :
    length = len(l)
    sum = 0
    for i in range(len(l)) :
        sum += l[i]

    average = int(sum / length)
    return average

def grade(score) :
    if score >= 90 : return 'A'
    elif score >= 80 : return 'B'
    elif score >= 70 : return 'C'
    else : return 'D'



print('*문제 1*')
s1 = [90, 90, 88]
s2 = [90, 95, 85, 90, 90]

avg1 = round(avg(s1), 0)
avg2 = round(avg(s2), 0)

s1.append(avg1)
s2.append(avg2)

s1.append(grade(avg1))
s2.append(grade(avg2))

print(s1)
print(s2)

print()
print('*문제 2*')
students = [[90, 90, 88], [100, 92, 90], [80, 90, 90], [85, 80, 90]]
tmp = 0
tmp1 = ''

print('** 리스트 변수 출력')
print(students)

for i in range(len(students)) :
    if tmp != 0 :
        tmp = 0
    tmp = avg(students[i])
    students[i].append(tmp)    
print('** 반복문(평균계산함수 호출) 실행 후')
print(students)

for j in range(len(students)) :
    if tmp1 != '' :
        tmp1 = ''
    tmp1 = grade(students[j][len(students[j])-1])
    students[j].append(tmp1)
print('** 반복문 (Grade 계산 함수 호출) 실행 후')
print(students)
