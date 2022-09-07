import random
import statistics as stats

rollLog =[]
rollNumber = 10

for x in range(rollNumber):
    rollLog.append(random.randrange(1,7))

print("Rolls: " + str(rollLog))
print("Population Variance: " + str(stats.pvariance(rollLog)))
print("Standard Deviation: " + str(stats.pstdev(rollLog)))



