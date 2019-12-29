import numpy as np
import pandas as pd
from Req_Func import get_freq

#initializing frequency array
freq = get_freq()
n = len(freq)
result = 0

#initilaizing numPy arrays for 2d with frequencies amd zeroes respectively
nullNP = np.zeros(n+1)
p = pd.Series(freq, index=range(1, n+1))#frequencies 
q = pd.Series(nullNP)#if we had unsuccessful searches, since null initilizing with zeroes

#test book declarations of e(freqencies), w(weights), r(root) initilaizing as dataframes with Pandas to compensate indexes
e = pd.DataFrame(np.diag(nullNP), index=range(1, n+2))
w = pd.DataFrame(np.diag(nullNP), index=range(1, n+2))
r = pd.DataFrame(np.zeros((n, n)), index=range(1, n+1), columns=range(1, n+1),dtype=int)

#The below code is from the Introduction to Algorithms 3rd Edition (Pg 402) Optimal BST
#Executing 3 loops (n^3 time)
for l in range(1, n+1):
    load = (l/1000)*100 #visual use only
    print("Calculating :","%.2f" %load,"%")
    for i in range(1, n-l+2):
        j = i+l-1
        e.set_value(i, j, np.inf)
        w.set_value(i, j, w.get_value(i, j-1) + p[j] + q[j])
        for k in range(i, j+1):
            t = e.get_value(i, k-1) + e.get_value(k+1, j) + w.get_value(i, j)
            if t < e.get_value(i, j):
                e.set_value(i, j, t)
                r.set_value(i, j, k)

#printing while matrix and storing the cost data into a file (OBST_Results.txt) on append mode
print(e)
print(r)
result = e[1000][1]
f=open("OBST_Results.txt","a+")
f.write("%d\n"%result)
f.close()