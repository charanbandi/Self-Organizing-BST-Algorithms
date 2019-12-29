from splay import get_splay 
from mtr import get_mtr
from dmt import get_dmt 

#hard coding obstvalues as it  runs n^3 and results are very tight bound ranges anyways
obst_arr = [83751,83436,83519,83538,83465,83562,83500,83678,83594,83170] 
splay_arr = []
mtr_arr = []
dmt_arr = []

obst_avg = splay_avg = mtr_avg = dmt_avg = 0

for x in range(10):
    print("Calculating :",(x+1)*10,"%")
    splay_arr.append(get_splay())
    exec(open("mtr.py").read())
    mtr_arr.append(get_mtr())
    exec(open("dmt.py").read())
    dmt_arr.append(get_dmt())

print("\n")
print("*** Costs of 10 Runs ***\n")
print("Optimal BST costs are:\t\t\t",obst_arr)
print("Splay costs are:\t\t\t",splay_arr)
print("Move to root costs are:\t\t\t",mtr_arr)
print("Dynamic Monotone Tree costs are:\t",dmt_arr)
print("\n")

for x in range(10):
    obst_avg += obst_arr[x]
    splay_avg += splay_arr[x]
    mtr_avg += mtr_arr[x]
    dmt_avg += dmt_arr[x]

obst_avg /= 10
splay_avg /= 10
mtr_avg /= 10
dmt_avg /= 10
print("** Averages of each Algorithm ***")
print("\nOptimal BST :\t\t\t",obst_avg,"\nSplay :\t\t\t\t",splay_avg,"\nMove to Root :\t\t\t",mtr_avg,"\nDynamic Monotone Tree :\t\t",dmt_avg,"\n")
print("\n*** Static Competitive Ratio ***\n")
print("Splay Tree :\t\t","%.3f"%(splay_avg/obst_avg),"\nMove to Root :\t\t","%.3f"%(mtr_avg/obst_avg),"\nDynamic Monotone :\t","%.3f"%(dmt_avg/obst_avg),"\n")

def obst_score():
    return obst_arr
def splay_score():
    return splay_arr
def mtr_score():
    return mtr_arr
def dmt_score():
    return dmt_arr