from time import time
from sys import argv
from os import system

times = []

for i in range(100):
    start = time()
    
    system(argv[1])

    finish = time()

    elapsed = start-finish
    
    times.append(elapsed)
    
    continue

avg = sum(times)/len(times)

print "Average elapsed time", abs(avg)
