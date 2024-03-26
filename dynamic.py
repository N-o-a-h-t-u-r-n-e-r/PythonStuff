import time
import random

def dynamic(values, weights, maxCap, items):
    G = [[0] * (maxCap + 1) for _ in range(items + 1)]

    for i in range(items + 1):
        for c in range(maxCap + 1):
            if i == 0 or maxCap == 0:
                G[i][c] = 0
            elif weights[i-1] <= c:
                G[i][c] = max(values[i-1] + G[i-1][c-weights[i-1]], G[i-1][c])
            else:
                G[i][c] = G[i-1][c]
    return G[items][maxCap]



#values = [60, 100, 120]
#weights = [10, 20, 30]
#maxCap = 50

values = [random.randint(11, 10000) for _ in range(10000)]
weights = [random.randint(11, 10000) for _ in range(10000)]
maxCap = 1000

items = len(values)
startTime = time.time()
print("Final Value: ", dynamic(values, weights, maxCap, items))
endTime = time.time()
total = endTime - startTime
print("Runtime: ", total)