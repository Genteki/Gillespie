import pandas as pd
import numpy as np
import json
import sys

config = json.load(open("config.json"))
projPath = config["projectPath"]
sys.path.append(projPath)
from algorithm.simulator import *



# 1 Db->Db+P, rb
# 2 Db->Du, kb
# 3 Db->Du+P, su
# 4 Du->Du+P, ru
# 5 Du+P-> Db, sb
# 6 P->None, kf

# parameters
rho_u = 60;sigma_b = .004;rho_b = 25;sigma_u = .25;theta = 0
# rho_u = 60; theta = 0; sigma_b = 0.004 ; rho_b = 5; sigma_u = .5
kf = 1
ru = rho_u*kf
rb = rho_b*kf
kb = theta*kf
su = sigma_u*kf
sb = sigma_b*kf

# reactions
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
# reaction parameters
rates = np.array([rb, kb, su, ru, sb, kf])
# intial state
ss = np.array([1, 0, 0])
# initialize the system
system = gillespieSystem(3, ss, reactant, products, rates)
# time to reach steady-state
t_ss = 10
# maxtime
tMax = 11
# repeat time
N = 2000
# data
n=None
newHistory = system.simulate(tMax)
n = np.array([])

# loop start
for i in range(N):
    newHistory = system.simulate(tMax)
    for j in range(newHistory.shape[0]):
        if newHistory[j, 0] > t_ss:
            newHistory = newHistory[j:].T[3]
            print("No.", i+1, "simulation", newHistory.mean())
            n = np.append(n,newHistory.mean())
            break

# plot
'''
(count, bins, ignored) = plt.hist(n, bins=np.linspace(0,99,50), density=True)
plt.close()
'''
sns.set_style("whitegrid")
fig = plt.figure()
ax = fig.subplots()
ax.set_xlabel("protein")
ax.set_ylabel("P(n)")
ax.set_title("kf = 1, [Du,Db,p] = [1,0,0]")
# ax.plot(bins[1:], count)
y, bins, patches = plt.hist(n, bins=50,range=(0,100),density=True)
fig.savefig("output/theta.png", dpi=300)
