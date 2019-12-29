from final_run import obst_score,splay_score,mtr_score,dmt_score

obst_score = obst_score()
splay_score = splay_score()
mtr_score = mtr_score()
dmt_score = dmt_score()

from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
import numpy as np


plt.style.use('dark_background')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

num = (obst_score,splay_score,mtr_score,dmt_score)
colors = ['purple', 'g', 'y', 'r']
yticks = [3, 2, 1, 0]
yticklab = ['DMT','MTR','Splay','OBST']

for c, k in zip(colors, yticks):
    xs = np.arange(10)
    ys = num[k]
    cs = [c] * len(xs)
    ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.7)#70% opacity

ax.set_xlabel('Index for 10 runs')
ax.set_ylabel('Algorithms')
ax.set_zlabel('Cost per Run')
ax.set_yticklabels(yticklab)
ax.labelsize : 10
ax.set_yticks(yticks)

plt.show()