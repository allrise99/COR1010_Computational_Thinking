#2020 기말고사

print('문제 1')
score = []
score = input("학생들 성적? ").split()
stunum = {}

for i in range(0,len(score)) :
    stunum[score[i]] = stunum.get(score[i], 0)+1

for j in stunum :
    print(j,'점', stunum[j],'명', end = ' ')

'''
print()
print('문제 2')

bday = {}
tmp = ()

while(True) :
    tmp = input().split()
    bday[tmp[2]] = tmp 
    if bday[i] == '' :
        break

print(bday)
'''
