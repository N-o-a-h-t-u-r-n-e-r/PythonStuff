import time
import random

def greedy(values, weights, maxCap):
  
    items = list(zip(values, weights))
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    
    G = []
    cap = maxCap
    total = 0
    
    for item in items:
        if item[1] <= cap:
            G.append(item)
            cap -= item[1]
            total += item[0]
    
    return G, total

#values = [60, 100, 120]
#weights = [10, 20, 30]
#maxCap = 50

values = [random.randint(11, 10000) for _ in range(10000)]
weights = [random.randint(11, 10000) for _ in range(10000)]
maxCap = 1000

startTime = time.time()
result, total = greedy(values, weights, maxCap)
#print("Items in knapsack:", result)
print("Final Value: ", total)
endTime = time.time()
total = endTime - startTime
print("Runtime: ", total)