import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import pandas as pd
file = open("C:\\Users\\bandi\\Documents\\work\\GMU\\583\\Algorithms Project\\583 Project File\\OBST compiled results\\OBST_Results.txt","r")
values = [line.rstrip('\n') for line in file] 
values = list(map(int, values))
ind = [1,2,3,4,5,6,7,8,9,10]
x_pos = [i for i, _ in enumerate(ind)]
plt.bar(x_pos, values, color='green',width=0.5)
plt.xticks(x_pos, ind)
plt.xlabel("Run Index")
plt.ylabel("Cost of Search")
plt.title("Cost of Static OBST over 10 runs")
plt.show()

average = 0
for x in range(len(values)):
    average += values[x]
average = average/10
average = int(average)
print(average)