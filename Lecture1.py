
# coding: utf-8

# In[6]:

x,y,z = "May"


# In[2]:

print(x,y,z)


# In[3]:

p, *q = 'Bill'


# In[4]:

print(p,q)


# In[7]:

a = b = 0


# In[8]:

print(a,b)


# In[9]:

L = [1,2]
M = L
L += [3,4]
L,M


# In[11]:

print(a,b,sep=" and is ")


# In[12]:

# same variable names in different files reference the same values. So if value is changed in one file then it 
# will reflect in other file too.


# In[13]:

temp = 5
if temp == 1:
    print("temp is 1")
elif temp == 7:
    print("temp is 7")
else:
    print("temp is 5")


# In[17]:

n = 100
while n>0:
    n = n / 10
    print(n)


# In[21]:

# Parallel Traversals: zip
L1 = [1,2,3,4,5]
L2 = [5,6,7,8,10,5]
list(zip(L1, L2))
for (x, y) in zip(L1, L2):
    print(x, y, '--', x+y)


# In[22]:

for x in [1, 2, 3, 4]: print(x ** 2, end=' ')


# In[23]:

# Iterator vs Comprehension 
L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 10
print(L)
print("-----"*5)
print("-----"*5)


# In[24]:

L = [x + 10 for x in L]
print(L)
print("-----"*5)
print("-----"*5)


# In[25]:

r2d2 = [x + y for x in 'abc' for y in 'lmn']
print(r2d2)


# In[26]:

x  = [1,2,3,4,5,6]


# In[29]:

for (b+2) in x:
    print(x[b])


# In[34]:

for i in range(len(x)):
    i = i * 2
    print(x[i])
    


# In[35]:


L = []
L = [123, 'abc', 1.23, {}]
L = ['Bob', 40.0, ['dev', 'mgr']]
L = list('spam')                      # ['s','p','a','m']
L = list(range(-4, 4))        

[1, 2, 3] + [4, 5, 6]

res = [c * 4 for c in 'SPAM']


# In[37]:

print(res)


# In[38]:

print(res[-2])


# In[39]:

L[2]


# In[40]:

L[-2]


# In[41]:

L.sort()


# In[42]:

L


# In[43]:

res.sort()


# In[44]:

res


# In[45]:

L.sort(key=res.lower)


# In[46]:

D = {}
D = {'name': 'Bob', 'age': 40}
E = {'cto': {'name': 'Bob', 'age': 40}}       # Nesting
D['name']
D.keys()
D.values()
D.get('height', 88)  


# In[47]:

D.get('name')


# In[48]:

D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}   
D = {x: x ** 2 for x in [1, 2, 3, 4]}   


# In[49]:

D


# In[50]:

D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])} 


# In[51]:

D


# In[55]:

# D.keys().sort() --- CHECK THIS !!!!!!!!!


# In[53]:

S = r'Knight"s'


# In[54]:

S


# In[56]:

S = r"Knight's"


# In[57]:

S


# In[59]:

S = 'abcdefghijklmnop'
S[1:10:2]
    


# In[60]:

S[::2]


# In[61]:

S[::−1] # CHECK THIS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# In[62]:

def intersect(seq1, seq2): 
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x) 
    return res


# In[63]:

s1 = "SPAM"
s2 = "SCAM"
y = intersect(s1, s2)
x = intersect([1, 2, 3], (1, 4))  


# In[64]:

y


# In[65]:

x


# In[ ]:



