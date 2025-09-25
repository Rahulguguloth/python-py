#!/usr/bin/env python
# coding: utf-8

# In[1]:


r=float(input("Enter radius"))
a=3.14*r*r
print(a)


# In[2]:


s=input()
v="aeiouAEIOU"
c=0
for char in s:
    if char in v:
        c+=1
print(c)


# In[7]:


s=input()
v="aeiouAEIOU"
c=0
con=0
for char in s:
    if char in v:
        c+=1
    else:
        con+=1        
print(c)
print(con)


# In[14]:


l=[30,42,56,70,45,35 ]
for i in range (len(l)):
    if l[i] % 5==0:
        l[i] -= 5
print(l)
    


# In[21]:


l=list(map(int,input().split()))
j=[]
p=[]
for i in l:
    if i%2==0:
        j.append(i)
    else:
        p.append(i)
print(j)
print(p)
    


# In[23]:


l=list(map(int,input().split()))
j=0
p=0
for i in l:
    if i%2==0:
        j=j+i
    else:
        p=p+i
print(j)
print(p)
    


# In[35]:


n = list(map(int, input().split()))

e = 0
o = 0
for i, num in enumerate(n):
    if num % 2 == 0:  
        e += i
    else:
        o += i
print("even =",e)
print("odd =",o)


# In[34]:


n = [20,35,45,60,30,75,85,45,25,40]
e = 0
o = 0
for i in range(len(n)):     
    if n[i] % 2 == 0:       
        e+= i
    else:
        o+= i
print("even =",e)
print("odd =",o)


# In[36]:


li=["Mumbai","Hyd","delhi","Dubai","Jaipur","Kolkata","Dadar","Danish"]
a=[]
for i in li:
    if i[0]=="D" or i[0]=="d":
        a.append(i)
print(a)


# In[37]:


li=["Mumbai","Hyd","delhi","Dubai","Jaipur","Kolkata","Dadar","Danish"]
st=[50,40,30,20,50,48,39,78]
c=dict(zip(li,st))
print(c)


# In[43]:


a = {'Mumbai': 550, 'Hyd': 440, 'delhi': 30, 'Dubai': 20, 'Jaipur': 504, 'Kolkata': 48, 'Dadar': 39, 'Danish': 78}
b = []
for city, value in a.items():
    if value < 100:
        b.append(city)
print(b)


# In[46]:


a = {'Mumbai': 550, 'Hyd': 440, 'delhi': 30, 'Dubai': 20, 'Jaipur': 504, 'Kolkata': 48, 'Dadar': 39, 'Danish': 78}
for i in a:
    if a[i]<100:
          print(i)


# In[61]:


def print_small_values(a):
    for i in a:
        if a[i] < 100:
            print(i)

# Example dictionary
a = {
    'Mumbai': 550,
    'Hyd': 440,
    'delhi': 30,
    'Dubai': 20,
    'Jaipur': 504,
    'Kolkata': 48,
    'Dadar': 39,
    'Danish': 78
}

print_small_values(a)


# In[62]:


def circle_area(r):
    a = 3.14 * r * r
    return a
radius = float(input("Enter radius: "))
print("Area of circle:", circle_area(radius))


# In[60]:


def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count,consonant_count
s = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(s)
print("Vowels:",vowels)
print("Consonants:",consonants)


# In[ ]:




