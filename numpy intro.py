#!/usr/bin/env python
# coding: utf-8

# # Basic Functions

# In[47]:


import numpy as np

a = np.zeros((2,2))
print(a)

b = np.ones((2,3))
print(b)

c = np.full((2,3),5)
print(c)

print()
d = np.eye(3)
print(d)

e = np.arange(1,21)
f = e.reshape((4,5))
print(f)


# # Slicing

# In[45]:


import numpy as np

data = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
a = np.array(data)

bool_i = (a%2==0)

print(a[bool_i])


b = a[a%2 == 0]
print(b)


# 

# # Array Calculation

# In[55]:


import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])

c = a + b
print(c)

c = np.multiply(a, b)
print(c)

c = np.divide(a, b)
print(c); print()


d = np.array([1,2,3]); e = np.array([10,20,30])
print(2*d)

#1차원 배열에서의 연산
print()
data = [1,2,3]
a = np.array(data)
a = 2*a
print(a)

#리스트에서 연산
a = [1,2,3]
for i in range(len(a)) :
    a[i] = a[i] * 2
print(a)


# In[59]:


import numpy as np

a = np.array([[1,2],[3,4]])
s = np.sum(a)
print(s)

s = np.sum(a, axis=0)
print(s)

s = np.sum(a, axis = 1)
print(s)

s = np.prod(a)
print(s)


# # Using Matplotlib

# In[68]:


import matplotlib.pyplot as plt

y= np.array([1178.5,1089.39,1319.37,1468.28,
897.3,1197.05,150.88,171.17])

x= np.array(['USD', 'JPY', 'EUR', 'GBP', 'CAD', 'CHF','HKD', 'CNY'])

plt.plot(x, y, 'bs:')
plt.show()
             


# # Pandas

# In[74]:


import pandas as pd

#1차원 자료구조 Series
data = [1,3,5,7,9]
s = pd.Series(data, index = ['아이린','슬기','웬디','조이','예리'])
print(s); print()

print(s.values)
print(s.index); print()

input2 = pd.Series({'England':'London', 'Canada':'Ottawa'})
print(input2)


# In[81]:


import pandas as pd

g_data = { 'year': [2016,2017,2018], 'GDP_rate ': [2.8, 3.1, 3.0],
           'GDP': ['1.63M','1.73M','1.83M']}

df = pd.DataFrame(g_data)
print(df)

print(df.GDP)
print(df.loc[1]); print()

names = ['Bob', 'Jessica', 'Mary', 'John', 'Kate']
birth = ['12-15', '10-11', '05-05', '12-03', '04-21']
member = {'Name' : names, 'Birth' : birth}
dfM = pd.DataFrame(member)
print(dfM)


# # 실습

# In[89]:


import pandas as pd
import matplotlib.pyplot as plt

data = {'고시일' : ['8.12', '8.13', '8.14', '8.16', '8.19', '8.20'], 
        '매매기준' : [58905.51, 59898.99, 58573.80, 58829.29, 58397.18, 58137.71]}

df = pd.DataFrame(data)
print(df)

x= df['고시일']
y= df['매매기준']

plt.plot(x, y, 'bs--')
plt.title('2019/8 GOLD(1g) rate')
plt.show()

             

