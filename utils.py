from abr import *
import random
import math
import matplotlib.pyplot as plt
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

def count_nonzero_elements(lst):
        count = 0
        for x in lst:
            if x != 0:
                count += 1
        return count
def compute_nodes_repetitions(nodes_list, max_key):
    counts = [0] * (max_key+1)
    for node in nodes_list:
        counts[node.key] += 1
    return counts

    

def compute_ranges(n, percentages):  #Restituisce i ranges per ottenere determinate percentuali di chiavi duplicate
    ranges = []
    for perc in percentages:
        target_frac = perc / 100.0

        def dup_frac(m):
            distinct_expected = m * (1 - math.exp(-n / m))
            return 1 - distinct_expected / n

        if target_frac <= 0:
            ranges.append(float('inf'))
            continue

        m_low, m_high = 1, max(2, int(n * 2))
        while dup_frac(m_high) > target_frac:
            m_high *= 2

        for _ in range(50):
            m_mid = (m_low + m_high) / 2
            if dup_frac(m_mid) > target_frac:
                m_low = m_mid
            else:
                m_high = m_mid

        ranges.append(int(round(m_mid)))

    return ranges
