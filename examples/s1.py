import json
import sys
config = json.load(open("config.json"))
projPath = config["projectPath"]
sys.path.append(projPath)

import numpy as np
import pandas as pd
from algorithm.simulator import *


# 1 Db->Db+P, rb
# 2 Db->Du, kb
# 3 Db->Du+P, su
# 4 Du->Du+P, ru
# 5 Du+P-> Db, sb
# 6 P->None, kf

'''  
    [Du,Db,P]
[
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [1,0,0],
    [1,0,1],
    [0,0,1]
]
[
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,0,1],
    [0,1,1],
    [0,0,0]
]
[rb,kb,su,ru,sb,kf]
''' 
rho_u = 60; sigma_b=.004; rho_b = 25; sigma_u=.25
theta = 0
kf = .1
ru = rho_u*kf
rb = rho_b*kf
kb = theta*kf
su = sigma_u*kf
sb = sigma_b*kf

reactant = np.array([   
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 0, 1],
    [0, 0, 1]   
])
products = np.array([
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 0]
])
rates = np.array([rb, kb, su, ru, sb, kf])
ss = np.array([2,2,0])
system = gillespieSystem(3,ss,reactant,products,rates)

# simualtion
t_max = 200
N = 200
hist_sum = system.simulate(t_max)[:5000]
for i in range(N-1):
    print("No.", i, " example")
    new_hist = system.simulate(t_max)
    if new_hist.shape[0] <= 5000:
        i = i - 1
        break
    hist_sum += new_hist[:5000]
hist_sum /= N

his = pd.DataFrame(hist_sum, columns=["t", "Du", "Db", "p"])

sns.set_style("whitegrid")
fig = plt.figure()
ax = fig.subplots()
ax.set_xlabel("time")
ax.set_ylabel("quantity of p")
ax.set_title("kf = 0.1, [Du,Db,p] = [2,2,0]")
ax.plot(his["t"], his["p"])
fig.savefig("output/s1.png", dpi=300)

