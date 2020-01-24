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
rho_u = 60
sigma_b = .004
rho_b = 25
sigma_u = .25
theta = 0
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
ss = np.array([1, 1, 0])
# initialize the system
system = gillespieSystem(3, ss, reactant, products, rates)
# time to reach steady-state
t_ss = 20
# maxtime
tMax = t_ss*5
# repeat time
N = 100
# data
n=None
newHistory = system.simulate(tMax)
for j in range(newHistory.shape[0]):
    if newHistory[j, 0] > t_ss:
        newHistory = newHistory[j:].T[3]
        n = newHistory
        break

# loop start
for i in range(N):
    newHistory = system.simulate(tMax)
    for j in range(newHistory.shape[0]):
        if newHistory[j, 0] > t_ss:
            print("No.", i+1, "simulation")
            newHistory = newHistory[j:].T[3]
            n = np.append(n,newHistory)
            break

# plot
(count, bins, ignored) = plt.hist(n, bins=range(100), density=True)
plt.close()
sns.set_style("whitegrid")
fig = plt.figure()
ax = fig.subplots()
ax.set_xlabel("protein")
ax.set_ylabel("P(n)")
ax.set_title("kf = 0.1, [Du,Db,p] = [1,0,0]")
ax.plot(range(0,99), count)
fig.savefig("output/theta2.png", dpi=300)