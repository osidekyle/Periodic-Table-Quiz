#!/usr/bin/env python
# coding: utf-8

# In[40]:


entered = []


# In[41]:


def answer_getter():
    while len(entered) < 5:
        enter = input("Enter an element:")
        if enter in entered:
            print("No duplicates allowed\n")
        else:
            entered.append(enter.lower())


# In[43]:


print("Enter the name of 5 of the first 20 elements on the periodic table of elements\n")
answer_getter()


# In[44]:


get_ipython().system('curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt')


# In[45]:


twenty_elements = open("elements1_20.txt","r")


# In[46]:


true_elems=[]
one_elem = ''


# In[47]:


for item in range(20):
    one_elem = twenty_elements.readline().lower()
    true_elems.append(one_elem.strip().lower())


# In[48]:


print(true_elems)


# In[49]:


correcto = []
incorrecto = []


# In[50]:


for words in entered:
    if words.lower() in true_elems:
        correcto.append(words)
    else:
        incorrecto.append(words)


# In[51]:



percen = len(correcto)*20


# In[52]:


print("Quiz score:",percen,"% correct\n")
print("Correct answers:",correcto)
print("Incorrect answers:",incorrecto)

