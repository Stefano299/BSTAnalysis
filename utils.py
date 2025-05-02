from abr import *
import random
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from time import perf_counter

def measureTime(algorithm, *args):
    start = perf_counter()
    algorithm(*args)
    end = perf_counter()
    return end - start
  
def createAndShowPlt(xArr, yArr1, xLabel, yLabel, title, label1=None, yArr2=None, label2=None, yArr3=None, label3=None):
    plt.plot(xArr, yArr1, label=label1 if label1 is not None else None)
    if yArr2 is not None:
        plt.plot(xArr, yArr2, label=label2 if label2 is not None else None)
    if yArr3 is not None:
        plt.plot(xArr, yArr3, label=label3 if label3 is not None else None)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
    
def generateRandomNodes(n, maxN):
    nodes = []
    for _ in range(n):
      key = random.randint(1, maxN)
      nodes.append(Node(key))
    return nodes
