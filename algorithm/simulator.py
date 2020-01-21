import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import sys

config = json.load(open('config.json'))
projPath = config["projectPath"]
sys.path.append(projPath)

class gillespieSystem:
    '''
        init_ss: intitial state space
        n: number of materials
        reactants/products: matrix of reactants/products
        cr: reaction coefficient
    '''
    def __init__(self, n, init_ss, reactants=np.array([[]]), products=np.array([[]]), cr=np.array([])):
        self.ss = init_ss
        self.n = n
        self.reactants = reactants
        self.products = products
        self.cr = cr

    # add reaction
    # be careful that it doesnt check whether there exists same reactions in the matrix
    def addReaction(self, reactant, product, c):
        if (reactant.shape[0] != self.n) or (product.shape[0]!=self.n):
            print("size error: the two vector's size should be same as n")
            return
        
        if (self.reactants.size==0):
            self.reactants = np.array([reactant])
            self.products = np.array([product])
            self.cr = np.array([c])
            print(self.reactants, self.cr)
            return
        self.products = np.append(self.products, np.array([product]),axis=0)
        self.reactants = np.append(self.reactants, np.array([reactant]),axis=0)
        self.cr = np.append(self.cr, np.array([c]))
        return

    def getProspencities(self, ss):
        p = np.zeros(self.reactants.shape[0])
        prod = ss ** self.reactants
        for i in range(self.reactants.shape[0]):
            p[i] = np.product(prod[i])*self.cr[i]
        return p

    def getDeltaTime(self, p):
        return -np.log(np.random.random()) / p.sum()
    
    def getReaction(self, p):
        return np.random.choice(range(self.reactants.shape[0]), p=p/p.sum())
        
    def simulate(self, maxTime):
        t = 0
        ss = self.ss.copy()
        history = np.array([np.append([t], ss)])
        while t < maxTime:
            print(ss)
            p = self.getProspencities(ss)
            t += self.getDeltaTime(p)
            i = self.getReaction(p)
            ss = ss - self.reactants[i] + self.products[i]
            history = np.append(history, np.array([np.append([t],ss)]), axis=0)
        return history

def test():
    ss = np.array([1e2, 1e2, 0],dtype=np.int)
    reactants = np.array([
        [1, 1, 0]
    ], dtype=np.int)
    products = np.array([
        [0, 0, 1]    
    ], dtype=np.int)
    c = np.array([1e-4])
    system = gillespieSystem(3,ss)
    system.addReaction(np.array([1,1, 0]), np.array([0, 0, 1]), 1e-4)
    system.addReaction(np.array([0, 0, 1]), np.array([1, 1, 0]), 1e-2)
    his = system.simulate(100)
    print(his)

if __name__  == "__main__":
    test()



        

