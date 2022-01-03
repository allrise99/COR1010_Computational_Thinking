#실습 10-2

buffer = input("안녕하세요\n")
special = "~!@#$%^&*-_+=(){}[]:;?.,<>"
lbuffer = []

for i in range(0, len(buffer)) :
    if buffer[i] in special :
        lbuffer.append(" ")
    else :
        lbuffer.append(buffer[i])
        
buffer = "".join(lbuffer)
print("출력 1 : ", buffer)

#buffer : a.sd,s
#수정 후 : a sd s


list_buffer = buffer.split(" ")
print("출력 2 : ", list_buffer)

dict_buffer = {}

#listbuffer : [a, sd, s]
'''
s -> db = 0 -> 1
s -> db = 1 
'''

for word in list_buffer :
    dict_buffer[word] = dict_buffer.get(word, 0) + 1

print(dict_buffer)
