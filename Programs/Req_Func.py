import random

#Generates Index with random permutation Algorithm from Textbook (pg 126)
def get_index():
    key_array = []
    for i in range(1,1001):
        key_array.append(i)
    length = len(key_array)
    for i in range(length):
        j = random.randint(i,length-1)#random includes ceiling value also hence-1
        key_array[i],key_array[j] = key_array[j],key_array[i]
    return key_array


freq = []
a = []
c = [0]
for i in range(1000):
    freq.append(0)
index = []
for i in range(1000):
    j = random.randint(1,100)
    a.append(j)
    c.append(j+c[i])
A = c[-1] #last node total  
for k in range(10000):
    j = random.randint(1,A)
    for k in range(len(c)):
        if(c[k-1]<j<=c[k]):
            index.append(k)
            freq[k-1] = freq[k-1]+1

#returns the Frequency list
def get_freq():
    return freq

#returns the Access sequence list
def get_accseq():
    return index