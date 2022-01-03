'''
def 생일찾기_함수(이름, 리스트):
    if name not in 리스트 :
        print("{} None!!".format(이름))
    else :
'''     


'''
print('문제 1')
score = input("학생들 성적? ")
slist = score.split()
sdict = {}

for scores in slist :
    sdict[scores+'점'] = sdict.get(scores+'점', 0)+1

for i in sdict :
    print(i, str(sdict[i])+'명', end = ' ')
'''

print('문제 2')
B = {}

while(True) :
    tmp = input() # 진 feb 13
    if tmp == '' :
        break
    
    tmplist = tmp.split() #[진, feb, 13]
    tmpdict = {}

    tmpdict[int(tmplist[2])] = tmplist[0]
    #{13 : '진'}
    
    B[tmplist[1]] = tmpdict
    #B : {feb : {13 : '진'}}


print(B)

'''
tmp1 = input() 
생일찾기_함수(tmp1, B)
'''
