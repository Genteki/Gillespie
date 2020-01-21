import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import sys

config = json.load(open('config.json'))
projPath = config["projectPath"]
sys.path.append(projPath)

'''
    here's just for simple reactions
    0    r_i        p_i
    1    A+B->C     Xa*Xb*c_1
    2    C->A+B     Xc*c_2 
'''

# state space [Xa,Xb,Xc].T
ss = [1e2, 1e2, 0]

# reactions
reactions = np.array([
    [-1, -1, 1],
    [1, 1, -1]
], dtype=np.int)

# reaction coefficient
c = np.array([1e-4, 1e-2])

# get the prospensities


def prospensitie(ss, c):
    return np.array([
        ss[0]*ss[1]*c[0], ss[2]*c[1]
    ])

# evolute


def evolute(init_ss, r, c, tMax):
    t = 0
    history = np.array([init_ss+[t]])
    ss = init_ss.copy()
    while t < tMax:
        p = prospensitie(ss, c)
        p0 = p.sum()
        p = p / p0
        dt = -np.log(np.random.random())/p0
        reaction_i = np.random.choice(range(reactions.shape[0]), p=p)
        for i in range(3):
            ss[i] += reactions[reaction_i, i]
        t = t+dt
        history = np.append(history, np.array([ss+[t]]), axis=0)
    return pd.DataFrame(history, columns=["A", "B", "C", "t"])


def main():
    sns.set_style("whitegrid")
    fig = plt.figure()
    ax = fig.subplots()
    his = evolute(ss, reactions, c, 1000)
    ax.plot(his["t"], his["A"])
    ax.plot(his["t"], his["C"])
    fig.savefig("output/output1.png",dpi=300)

if __name__ == "__main__":
    main()
