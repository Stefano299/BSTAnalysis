from abr import *
import random
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from time import perf_counter

def measure_time(algorithm, *args):
    start = perf_counter()
    algorithm(*args)
    end = perf_counter()
    return end - start
  
def create_and_show_plt(x_arr, y_arr1, x_label, y_label, title, label1=None, y_arr2=None, label2=None, y_arr3=None, label3=None):
    plt.plot(x_arr, y_arr1, label=label1 if label1 is not None else None)
    if y_arr2 is not None:
        plt.plot(x_arr, y_arr2, label=label2 if label2 is not None else None)
    if y_arr3 is not None:
        plt.plot(x_arr, y_arr3, label=label3 if label3 is not None else None)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
    
def generate_random_nodes(n, max_n):
    nodes = []
    for _ in range(n):
      key = random.randint(1, max_n)
      nodes.append(Node(key))
    return nodes
